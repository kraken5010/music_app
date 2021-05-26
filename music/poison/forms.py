from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *


# Форма добавления фото
# class AddPhotoForm(forms.ModelForm):
#     class Meta:
#         def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             self.fields['album'].empty_label = "Категория не выбрана"
#
#         model = Photo
#         fields = ['photo', 'album']
#         widgets = {
#             'photo': forms.ImageField(attrs={'class': 'form-input'}),
#             'album': forms.ModelChoiceField(queryset=Album.objects.all())
#         }


# Форма регистрации пользователя
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login*', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email*', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password*', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Re-enter password*', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User    # стандартно
        fields = ('username', 'email', 'password1', 'password2')    # отображает поля


# Форма авторизации пользователя
class LoginUserForm(AuthenticationForm):    # создание своей формы авторизации
    username = forms.CharField(label='Login*', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password*', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


# Форма обратной связи
class FeedbackForm(forms.Form):
    name = forms.CharField(label='Your name*', max_length=255)
    email = forms.EmailField(label='Your email*')
    text = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':16, 'class': 'form-connect'}))



