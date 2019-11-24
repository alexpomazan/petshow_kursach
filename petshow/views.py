from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from .models import *
import re
from django.urls import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.core.mail import BadHeaderError, send_mail
from .models import Article, Comment 
 
def home(request):
    count = User.objects.count()
    return render(request, 'base.html', {
        'count': count})

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

def articles(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5 ]
    return render(request, 'article.html', {'latest_articles_list': latest_articles_list})

def detail(request, article_id):
    try:
        a = Article.objects.get( id = article_id)
    except:
        raise Http404("Статья не найдена!")
    latest_comments_list = a.comment_set.order_by('-id')[:10]
    return render(request, 'detail.html', {'article': a, 'latest_comments_list': latest_comments_list})

def leave_comment(request, article_id):
    try:
        a = Article.objects.get( id = article_id)
    except:
        raise Http404("Статья не найдена!")
    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])
    return HttpResponseRedirect( reverse('detail', args=(a.id,)) )

def about_us(request):
    return render(request, 'about_us.html')

def cabinet(request):
    return render(request, 'cabinet.html')

def contactform(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender_name = auth.get_user(request).username
            sender_email = form.cleaned_data['email']
            message = message = "{0} has sent you a new message:\n\n{1} \n\n email user: {2}".format(sender_name, form.cleaned_data['message'], form.cleaned_data['email']) 
            send_mail(subject, message, sender_email, ['aleksey.pomazan@gmail.com'])
            # send email code goes here
            return HttpResponseRedirect('http://localhost:8000/thanks/')

    else:
        form = ContactForm()
    # Выводим форму в шаблон
    return render(request, 'contact.html', {'form': form, 'username': auth.get_user(request).username})

def thanks(reguest):
    thanks = 'thanks'
    return render(reguest, 'thanks.html', {'thanks': thanks})