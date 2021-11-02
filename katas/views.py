from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http.response import HttpResponse
from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404,
)
from django.urls import reverse
from django.views.generic import ListView

from .forms import KataAPIForm, KataForm
from .models import Exercise

import requests


@login_required
def get_katas(request):
    form = KataAPIForm(request.POST or None)

    # filter out katas in db
    katas_db = Exercise.objects.filter(owner=request.user)
    katas_db_id = { kata.cw_id: kata.cw_id for kata in katas_db}
    
    
    if request.method == 'POST' and form.is_valid():
        kata = form.save(commit=False)
        kata.owner = request.user
        kata.save()
        # TODO
        # flash success message and change redirect 
        # return redirect('katas:home')
        return HttpResponse('Success!')

    # Users API
    url = f"https://www.codewars.com/api/v1/users/{request.user.username}/code-challenges/completed?"
    
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        # TODO
        # flash error message and add redirect 
        print(err)
    
    data = r.json()
    
    # (have name, cw_id, languages at this point)
    katas = data['data']

    filtered_katas = []
    # Code Challenges API for additional kata data
    for kata in katas:
        if kata['id'] not in katas_db_id:
            kata['completedLanguages'] = ','.join(kata['completedLanguages'])
            try:
                r = requests.get(f"https://www.codewars.com/api/v1/code-challenges/{kata['id']}")
                r.raise_for_status()
            except requests.exceptions.HTTPError as err:
                # TODO
                # flash error message and add redirect 
                print(err)
            data = r.json()
            kata['description'] = data['description']
            kata['tags'] = ' '.join(data['tags'])
            kata['rank'] = data['rank']
            kata['url'] = data['url'] + '/solutions/'
            filtered_katas.append(kata)

    context = {
        "filtered_katas": filtered_katas,
        'form': form,
    }

    return render(request, 'katas/from_codewars.html', context)


@login_required
def kata_list_view(request):
    katas = Exercise.objects.filter(owner=request.user)
    context = {
        'katas': katas,
    }
    return render(request, 'katas/list.html', context)


@login_required
def kata_detail_view(request, slug):
    kata = get_object_or_404(Exercise, owner=request.user, slug=slug)
    context = {
        'kata': kata,
    }
    return render(request, 'katas/detail.html', context)


@login_required
def kata_create_view(request):
    form = KataForm(request.POST or None)
    context = {
        'form': form,
    }
    if request.method == 'POST' and form.is_valid():
        kata = form.save(commit=False)
        kata.owner = request.user
        kata.save()
        # TODO
        # flash success message
        return redirect(kata.get_absolute_url())
    return render(request, 'katas/create_update.html', context)


@login_required
def kata_update_view(request, slug):
    kata = get_object_or_404(Exercise, slug=slug, owner=request.user)
    form = KataForm(request.POST or None, instance=kata)
    context = {
        'form': form,
        'kata': kata,
    }
    if request.method == 'POST' and form.is_valid():
        form.save()
        # TODO
        # flash success message
        return redirect('katas:list')
    return render(request, 'katas/create_update.html', context)


@login_required
def kata_delete_view(request, slug):
    kata = get_object_or_404(Exercise, slug=slug, owner=request.user)
    if request.method == 'POST':
        kata.delete()
        #TODO
        # flash success message
        return redirect('katas:list')
    context = {
        'kata': kata,
    }
    return render(request, 'katas/delete.html', context)


@login_required
def detail_hx(request, slug):
    kata = get_object_or_404(Exercise, slug=slug, owner=request.user)
    context = {
        'kata': kata,
    }
    return render(request, 'katas/partials/detail_hx.html', context)


@login_required
def more_detail_hx(request, slug):
    kata = get_object_or_404(Exercise, slug=slug, owner=request.user)
    context = {
        'kata': kata,
    }
    return render(request, 'katas/partials/more_detail_hx.html', context)


@login_required
def update_hx(request, slug):
    kata = get_object_or_404(Exercise, slug=slug, owner=request.user)
    form = KataForm(request.POST or None, instance=kata)
    context = {
        'form': form,
        'kata': kata,
    }
    if request.method == 'POST' and form.is_valid():
        form.save()
        # TODO
        # success message
        return redirect('katas:detail_hx', slug=kata.slug)
    return render(request, 'katas/partials/kata_form.html', context)


@login_required
def delete_hx(request, slug):
    kata = get_object_or_404(Exercise, slug=slug, owner=request.user)
    if request.method == 'POST':
        kata.delete()
        # TODO
        # flash message
        return HttpResponse('')


@login_required
def search_view(request):
    query = request.GET.get('q')
    if query == None:
        query = ''
    qs = Exercise.objects.filter(owner=request.user).filter(
        Q(name__icontains=query) | Q(languages__icontains=query)
        | Q(description__icontains=query) | Q(tags__icontains=query)
        | Q(rank__icontains=query) | Q(notes__icontains=query)
    )
    
    context = {
        'katas': qs,
    }
    return render(request, "katas/partials/results.html", context)