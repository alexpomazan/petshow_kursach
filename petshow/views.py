from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.generic import CreateView

from .models import *
import re
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .forms import ContactForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.core.mail import BadHeaderError, send_mail
from .models import Article, Comment 
 
def home(request):
    count = User.objects.count()
    return render(request, 'base.html', {
        'count': count})

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш акккаунт был создан! Вы можете войти в него')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })
 
def login(request):
    return render(request, 'registration/login.html')


def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Ваш аккаунт был обновлен!')
            return redirect('profile')
 
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html',context)

def shows(request):
    
    return render(request, 'show/shows.html')


class CreatePetOnShow(CreateView):
    model = PetOnShow
    fields = ('nick', 'gender', 'age', 'breed', 'image', 'info')
    template_name = 'show/add_pet.html'
    success_url = reverse_lazy('mypets')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

@login_required
def mypets(request):
    if request.method == 'POST':
        pet = get_object_or_404(PetOnShow, id=request.POST['pet'])
        if not pet.show:
            if request.POST.get('show') in (PetOnShow.ShowChoices.DOGS, PetOnShow.ShowChoices.CATS):
                pet.show = request.POST['show']
                pet.save()
                return redirect('mypets')
    context = {
        'pets': request.user.pets.order_by('-id'),
    }
    return render(request, 'show/mypets.html', context=context)


@login_required
def start_show(request, slug):
    if request.user.is_superuser:
        if slug in (PetOnShow.ShowChoices.DOGS, PetOnShow.ShowChoices.CATS):
            PetOnShow.objects.filter(show=slug).update(can_vote_before_date=timezone.now())
            if slug == PetOnShow.ShowChoices.DOGS:
                return redirect('dogshow')
            else:
                return redirect('catshow')


@login_required
def stop_show(request, slug):
    if request.user.is_superuser:
        if slug in (PetOnShow.ShowChoices.DOGS, PetOnShow.ShowChoices.CATS):
            PetOnShow.objects.filter(show=slug).update(can_vote_before_date=None)
            if slug == PetOnShow.ShowChoices.DOGS:
                return redirect('dogshow')
            else:
                return redirect('catshow')


@login_required
def vote_plus(request, pet_id):
    pet = get_object_or_404(PetOnShow, id=pet_id)
    if not pet.likes.filter(id=request.user.id).exists():
        pet.likes.add(request.user)
        pet.save()
    if pet.show == PetOnShow.ShowChoices.DOGS:
        return redirect('dogshow')
    elif pet.show == PetOnShow.ShowChoices.CATS:
        return redirect('catshow')


@login_required
def vote_minus(request, pet_id):
    pet = get_object_or_404(PetOnShow, id=pet_id)
    if pet.likes.filter(id=request.user.id).exists():
        pet.likes.remove(request.user)
        pet.save()
    if pet.show == PetOnShow.ShowChoices.DOGS:
        return redirect('dogshow')
    elif pet.show == PetOnShow.ShowChoices.CATS:
        return redirect('catshow')


def dogshow(request):
    slug = PetOnShow.ShowChoices.DOGS
    context = {
        'pets': PetOnShow.objects.filter(show=slug),
        'title': 'Выставка собак',
        'slug': slug,
    }
    return render(request, 'show/show.html', context=context)


def catshow(request):
    slug = PetOnShow.ShowChoices.CATS
    context = {
        'pets': PetOnShow.objects.filter(show=slug),
        'title': 'Выставка кошек',
        'slug': slug,
    }
    return render(request, 'show/show.html', context=context)
    
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
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender_name = auth.get_user(request).username
            sender_email = form.cleaned_data['email']
            message = message = "Отправил вам новое сообщение{0}\n\n{1} \n\n Email пользователя: {2}".format(sender_name, form.cleaned_data['message'], form.cleaned_data['email']) 
            send_mail(subject, message, sender_email, ['aleksey.pomazan@gmail.com'])
            return HttpResponseRedirect('http://localhost:8000/thanks/')

    else:
        form = ContactForm()
    # Выводим форму в шаблон
    return render(request, 'contact.html', {'form': form, 'username': auth.get_user(request).username})

def thanks(reguest):
    thanks = 'thanks'
    return render(reguest, 'thanks.html', {'thanks': thanks})