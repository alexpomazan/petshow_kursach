from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phone_field import PhoneField
from .models import *

class FormComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        
        widgets = {'article': forms.HiddenInput(),
                   'author_name': forms.HiddenInput(),
                   'comment_text': forms.Textarea(attrs={'rows': 5, 'cols': 40})}

    def __init__(self, articleId, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['article'].queryset = Article.objects.filter(pk=articleId)
        self.fields['author_name'].queryset = User.objects.filter(pk=user.id)
        self.fields['article'].initial = Article.objects.get(pk=articleId)
        self.fields['author_name'].initial = User.objects.get(pk=user.id)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема письма: ', max_length=100, widget=forms.TextInput(attrs={'size':'40','class': 'form-control'}))
    email = forms.EmailField(label='Ваш Email: ')
    # phone = forms.PhoneField(blank=True, help_text='Contact phone number')
    message = forms.CharField(label='Сообщение: ', widget=forms.Textarea)

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
