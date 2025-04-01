from django.contrib.auth.decorators import login_required
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


@login_required(login_url='login')  # Перенаправляет на страницу входа, если не авторизован
def gallery_view(request):
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = GalleryImageForm()

    images = GalleryImage.objects.all()
    return render(request, 'gallery.html', {'images': images, 'form': form})