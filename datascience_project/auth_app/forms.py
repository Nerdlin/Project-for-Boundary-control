from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        error_messages = {
            'username': {
                'required': _('Имя пользователя обязательно.'),
                'unique': _('Пользователь с таким именем уже существует.'),
            },
            'password2': {
                'password_mismatch': _('Пароли не совпадают.'),
            },
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

