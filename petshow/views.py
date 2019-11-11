from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import *
import re
from django.http import Http404

def home(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'registration/login.html')

def signup(request):
    return render(request, 'registration/signup.html')

def cabinet(request):
    return render(request, 'cabinet.html')