from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Функция для входа
def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
        
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль')
            
    return render(request, 'main/login.html')

# Функция для регистрации
def register_view(request):
    if request.user.is_authenticated:
        return redirect('index')
        
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Проверка существует ли пользователь
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Пользователь с таким именем уже существует')
            return render(request, 'main/register.html')
            
        # Создание пользователя
        user = User.objects.create_user(username=username, password=password)
        user.save()
        
        # Автоматический вход после регистрации
        login(request, user)
        return redirect('index')
        
    return render(request, 'main/register.html')

# Функция выхода
def logout_view(request):
    logout(request)
    return redirect('login')

# Защищенные маршруты (требуют авторизации)
@login_required(login_url='login')
def index(request):
    return render(request, 'main/index.html')

@login_required(login_url='login')
def history(request):
    return render(request, 'main/history.html')

@login_required(login_url='login')
def features(request):
    return render(request, 'main/features.html')

@login_required(login_url='login')
def gallery(request):
    return render(request, 'main/gallery.html')

@login_required(login_url='login')
def skills(request):
    return render(request, 'main/skills.html')

@login_required(login_url='login')
def feedback(request):
    return render(request, 'main/feedback.html')
