from django.urls import path

from .views import get_katas

urlpatterns = [
    path('', get_katas, name='get_katas')
]