from django.shortcuts import render, redirect
from .models import Project

from .forms import ProjectForm

import requests


def get_katas(request):
    form = ProjectForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        kata = form.save()
        return redirect('pages:home')

        
    url = f"https://www.codewars.com/api/v1/users/{request.user.username}/code-challenges/completed?"
    
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    
    data = r.json()
    katas = data['data']
    first = katas[0]

    for kata in katas:
        try:
            r = requests.get(f"https://www.codewars.com/api/v1/code-challenges/{kata['id']}")
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        data = r.json()
        kata['description'] = data['description']
        kata['tags'] = data['tags']
        kata['rank'] = data['rank']
        kata['url'] = data['url']
        

        # print(data['name'])
        # print(data['name'])
    first = katas[0]
    print(first)
    
    context = {
        "katas": katas,
        'form': form
    }
    # if request.method == 'POST' and form.is_valid():
    #     kata = form.save()
    #     return redirect('pages:home')

    return render(request, 'projects/list.html', context)



# def get_katas(request):
#     form = ProjectForm(request.POST or None)
#     url = f"https://www.codewars.com/api/v1/users/{request.user.username}/code-challenges/completed?"
    
#     try:
#         r = requests.get(url)
#         r.raise_for_status()
#     except requests.exceptions.HTTPError as err:
#         print(err)
    
#     data = r.json()
#     katas = data['data']
#     first = katas[0]

#     for kata in katas:
#         try:
#             r = requests.get(f"https://www.codewars.com/api/v1/code-challenges/{kata['id']}")
#             r.raise_for_status()
#         except requests.exceptions.HTTPError as err:
#             print(err)
#         data = r.json()
#         kata['description'] = data['description']
#         kata['tags'] = data['tags']
#         kata['rank'] = data['rank']
#         kata['url'] = data['url']
        

#         # print(data['name'])
#         # print(data['name'])
#     first = katas[0]
#     print(first)
    
#     context = {
#         "katas": katas,
#         'form': form
#     }
#     if request.method == 'POST' and form.is_valid():
#         kata = form.save()
#         return redirect('pages:home')

#     return render(request, 'projects/list.html', context)
