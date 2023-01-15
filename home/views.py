from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home/welcome.html', {})

@login_required
def authorized(request):
    return render(request, 'home/authorised.html', {})
