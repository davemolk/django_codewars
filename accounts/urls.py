from django.urls import path
from .views import SignupPageView, UpdateUsernameView


urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
]