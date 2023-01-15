from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
  

class AuthorizedView(LoginRequiredMixin,TemplateView):
    template_name = 'home/authorised.html'
    login_url = '/admin'