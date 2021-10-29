from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404,
)
from django.urls import reverse

from .forms import KataAPIForm, KataForm
from .models import Exercise

import requests


@login_required
def get_katas(request):
    form = KataAPIForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        kata = form.save(commit=False)
        kata.owner = request.user
        kata.save()
        # TODO
        # flash success message and change redirect 
        return redirect('pages:home')

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
    # have name, cw_id, languages
    katas = data['data']

    # Code Challenges API for additional kata data
    for kata in katas:
        try:
            r = requests.get(f"https://www.codewars.com/api/v1/code-challenges/{kata['id']}")
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            # TODO
            # flash error message and add redirect 
            print(err)
        data = r.json()
        kata['description'] = data['description']
        kata['tags'] = data['tags']
        kata['rank'] = data['rank']
        kata['url'] = data['url']
        
    context = {
        "katas": katas,
        'form': form,
    }

    return render(request, 'katas/from_codewars.html', context)


@login_required
def kata_list_view(request):
    kata_list = Exercise.objects.filter(owner=request.user)
    context = {
        'kata_list': kata_list,
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