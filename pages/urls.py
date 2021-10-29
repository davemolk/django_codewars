from django.urls import path
from .views import HomePageView, AboutPageView, ProfilePageView


app_name='pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('profile/', ProfilePageView.as_view(), name='profile')
]