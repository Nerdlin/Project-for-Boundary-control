from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import GalleryImage
from .forms import GalleryImageForm

def index_view(request):
    return render(request, 'index.html')

def history_view(request):
    return render(request, 'history.html')

def features_view(request):
    return render(request, 'features.html')

def skills_view(request):
    return render(request, 'skills.html')

def gallery_view(request):
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)  # request.FILES нужен для обработки файлов
        if form.is_valid():
            form.save()  # Сохраняем изображение в базе данных и на сервере
            return redirect('gallery')  # Перенаправляем на ту же страницу
    else:
        form = GalleryImageForm()  # Пустая форма для GET-запроса

    images = GalleryImage.objects.all()  # Получаем все изображения из базы
    return render(request, 'gallery.html', {'images': images, 'form': form})

