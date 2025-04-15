from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
from django.shortcuts import render, redirect
from .models import GalleryImage
from .forms import GalleryImageForm

@login_required(login_url='login')  # Перенаправляет на страницу входа, если не авторизован
def index_view(request):
    return render(request, 'index.html')

@login_required(login_url='login')  # Перенаправляет на страницу входа, если не авторизован
def history_view(request):
    return render(request, 'history.html')

@login_required(login_url='login')  # Перенаправляет на страницу входа, если не авторизован
def features_view(request):
    return render(request, 'features.html')

@login_required(login_url='login')  # Перенаправляет на страницу входа, если не авторизован
def skills_view(request):
    return render(request, 'skills.html')


@login_required(login_url='login')  # Перенаправляет на страницу входа, если не авторизован
def gallery_view(request):
    form = GalleryImageForm()  # Инициализируем форму по умолчанию
    images = GalleryImage.objects.all()

    if request.method == 'POST':
        if 'delete_selected' in request.POST:
            selected_ids = request.POST.getlist('delete_images')
            GalleryImage.objects.filter(id__in=selected_ids).delete()
            messages.success(request, "Выбранные изображения удалены.")
        elif 'delete_all' in request.POST:
            GalleryImage.objects.all().delete()
            messages.success(request, "Все изображения удалены.")
        else:
            form = GalleryImageForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Изображение успешно загружено.")
            else:
                messages.error(request, "Ошибка при загрузке изображения.")
        return redirect('gallery')

    return render(request, 'gallery.html', {'images': images, 'form': form})