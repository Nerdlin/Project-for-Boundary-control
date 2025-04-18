from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import LoginForm, RegisterForm, CustomSetPasswordForm
import smtplib
from .models import User  # Импортируем модель User

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        else:
            print("Login form errors:", form.errors)  # Отладка
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            print("Register form errors:", form.errors)  # Отладка
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

class CustomPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        # Проверяем, существует ли пользователь с таким email
        if not User.objects.filter(email=email).exists():
            messages.error(self.request, "Такой почты не существует.")
            return self.form_invalid(form)

        try:
            return super().form_valid(form)
        except smtplib.SMTPAuthenticationError:
            messages.error(self.request, "Ошибка аутентификации SMTP. Проверьте настройки email.")
            return self.form_invalid(form)
        except smtplib.SMTPException as e:
            messages.error(self.request, f"Ошибка отправки письма: {str(e)}")
            return self.form_invalid(form)
        except Exception as e:
            messages.error(self.request, f"Произошла ошибка: {str(e)}")
            return self.form_invalid(form)

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

    def get_success_url(self):
        return reverse_lazy('password_reset_complete')