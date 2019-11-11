from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
import re
from django.http import Http404

def home(request):
    count = User.objects.count()
    return render(request, 'base.html', {
        'count': count
    })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


def login(request):
    return render(request, 'registration/login.html')


def cabinet(request):
    return render(request, 'cabinet.html')