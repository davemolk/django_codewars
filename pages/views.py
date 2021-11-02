from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView

User = get_user_model()


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ProfilePageView(TemplateView):
    template_name = 'profile.html'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username']
    action = 'Update'
    template_name = 'username_update.html'
    success_url = reverse_lazy('pages:profile')