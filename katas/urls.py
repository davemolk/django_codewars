from django.urls import path

from .views import get_katas_api


app_name='katas'
urlpatterns = [
    path('', get_katas_api, name='get_katas_api')
]