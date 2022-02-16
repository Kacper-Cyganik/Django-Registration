from django.shortcuts import render
from django.contrib.auth.models import User

def home(request):
    return render(request, 'basic_app/home.html')
