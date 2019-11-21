from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from .models import *
import re
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.core.mail import BadHeaderError, send_mail
 
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

def shows(request):
    return render(request, 'shows.html')

def article(request):
    return render(request, 'article.html')

def about_us(request):
    return render(request, 'about_us.html')

def cabinet(request):
    return render(request, 'cabinet.html')

def contactform(reguest):
    if reguest.method == 'POST':
        form = ContactForm(reguest.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender_name = auth.get_user(reguest).username
            sender_email = form.cleaned_data['email']
            message = message = "{0} has sent you a new message:\n\n{1} \n\n email user: {2}".format(sender_name, form.cleaned_data['message'], form.cleaned_data['email']) 
            send_mail(subject, message, sender_email, ['aleksey.pomazan@gmail.com'])
            # send email code goes here
            return HttpResponseRedirect('http://localhost:8000/thanks/')

    else:
        form = ContactForm()
    # Выводим форму в шаблон
    return render(reguest, 'contact.html', {'form': form, 'username': auth.get_user(reguest).username})

def thanks(reguest):
    thanks = 'thanks'
    return render(reguest, 'thanks.html', {'thanks': thanks})