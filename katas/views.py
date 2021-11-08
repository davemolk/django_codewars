import requests

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http.response import HttpResponse
from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404,
)

from .forms import KataAPIForm, KataForm
from .models import Exercise


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
        return HttpResponse('Success!')

    # Users API
    url = f"https://www.codewars.com/api/v1/users/{request.user.username}/code-challenges/completed?"
    
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    
    data = r.json()
    
    # (have name, cw_id, languages at this point)
    katas = data['data']

    filtered_katas = []

    # Code Challenges API for additional kata data
    for kata in katas:
        if kata['id'] not in katas_db_id:
            kata['completedLanguages'] = ', '.join(kata['completedLanguages'])
            try:
                r = requests.get(f"https://www.codewars.com/api/v1/code-challenges/{kata['id']}")
                r.raise_for_status()
            except requests.exceptions.HTTPError as err:
                print(err)
            data = r.json()

            kata['description'] = data['description']
            kata['tags'] = ', '.join(data['tags'])
            kata['rank']= data['rank']['name']
            kata['url'] = data['url'] + '/solutions/'
            filtered_katas.append(kata)

    context = {
        "filtered_katas": filtered_katas,
        'form': form,
    }

    return render(request, 'katas/from_codewars.html', context)


@login_required
def save_all_katas(request):
    form = KataAPIForm()

    # filter out katas in db
    katas_db = Exercise.objects.filter(owner=request.user)
    katas_db_id = { kata.cw_id: kata.cw_id for kata in katas_db}

    # Users API
    url = f"https://www.codewars.com/api/v1/users/{request.user.username}/code-challenges/completed?"
    
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    
    data = r.json()
    
    # (have name, cw_id, languages at this point)
    katas = data['data']

    # Code Challenges API for additional kata data
    for kata in katas:
        if kata['id'] not in katas_db_id:
            kata['completedLanguages'] = ', '.join(kata['completedLanguages'])
            try:
                r = requests.get(f"https://www.codewars.com/api/v1/code-challenges/{kata['id']}")
                r.raise_for_status()
            except requests.exceptions.HTTPError as err:
                print(err)
            data = r.json()

            kata['description'] = data['description']
            kata['tags'] = ', '.join(data['tags'])
            kata['rank']= data['rank']['name']
            kata['url'] = data['url'] + '/solutions/'
            kata['owner'] = request.user
            my_kata = Exercise.objects.create(name=kata['name'], 
                owner=kata['owner'], cw_id=kata['id'], languages=kata['completedLanguages'],
                description=kata['description'], tags=kata['tags'], rank=kata['rank'], 
                url=kata['url'], notes=''
            )
            my_kata.save()

    return redirect('katas:list')

    
@login_required
def kata_list_view(request):
    katas = Exercise.objects.filter(owner=request.user)
    context = {
        'katas': katas,
    }
    return render(request, 'katas/list.html', context)


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
        return redirect('katas:detail_hx', slug=kata.slug)
    return render(request, 'katas/partials/kata_form.html', context)


@login_required
def delete_hx(request, slug):
    kata = get_object_or_404(Exercise, slug=slug, owner=request.user)
    if request.method == 'POST':
        kata.delete()
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