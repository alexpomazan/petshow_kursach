from django import forms
from phone_field import PhoneField

class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема письма: ', max_length=100, widget=forms.TextInput(attrs={'size':'40','class': 'form-control'}))
    email = forms.EmailField(label='Ваш Email: ')
    # phone = forms.PhoneField(blank=True, help_text='Contact phone number')
    message = forms.CharField(label='Сообщение: ', widget=forms.Textarea)