from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phone_field import PhoneField
from .models import Profile

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