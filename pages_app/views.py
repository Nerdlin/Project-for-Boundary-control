from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import GalleryImage
from .forms import GalleryImageForm
from django.contrib.auth import get_user_model  # Импортируем get_user_model
from feedback_app.models import Feedback  # Убедитесь, что модель Feedback существует

User = get_user_model()  # Получаем пользовательскую модель

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


@login_required(login_url='login')
def gallery_view(request):
    form = GalleryImageForm()
    # Filter images to show only those uploaded by the current user
    images = GalleryImage.objects.filter(user=request.user)

    if request.method == 'POST':
        if 'delete_selected' in request.POST:
            selected_ids = request.POST.getlist('delete_images')
            # Filter out empty strings from selected_ids
            selected_ids = [id for id in selected_ids if id]
            if selected_ids:  # Only proceed if there are valid IDs
                # Only delete images that belong to the current user
                GalleryImage.objects.filter(id__in=selected_ids, user=request.user).delete()
                messages.success(request, "Выбранные изображения удалены.")
            else:
                messages.info(request, "Не выбрано ни одного изображения для удаления.")
        elif 'delete_all' in request.POST:
            # Only delete all images that belong to the current user
            GalleryImage.objects.filter(user=request.user).delete()
            messages.success(request, "Все изображения удалены.")
        else:
            form = GalleryImageForm(request.POST, request.FILES)
            if form.is_valid():
                # Associate the image with the current user before saving
                gallery_image = form.save(commit=False)
                gallery_image.user = request.user
                gallery_image.save()
                messages.success(request, "Изображение успешно загружено.")
            else:
                messages.error(request, "Ошибка при загрузке изображения.")
        return redirect('gallery')

    return render(request, 'gallery.html', {'images': images, 'form': form})

