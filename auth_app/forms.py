from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='Электронная почта', required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        error_messages = {
            'username': {
                'required': _('Имя пользователя обязательно.'),
                'unique': _('Пользователь с таким именем уже существует.'),
            },
            'email': {
                'required': _('Электронная почта обязательна.'),
                'unique': _('Пользователь с такой почтой уже существует.'),
            },
            'password2': {
                'password_mismatch': _('Пароли не совпадают.'),
            },
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)