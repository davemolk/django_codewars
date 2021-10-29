from django.shortcuts import render, redirect
from .models import Exercise

from .forms import KataAPIForm

import requests


def get_katas_api(request):
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

    return render(request, 'projects/list.html', context)
