from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import GalleryImage

def index_view(request):
    return render(request, 'index.html')

def history_view(request):
    return render(request, 'history.html')

def features_view(request):
    return render(request, 'features.html')

def gallery_view(request):
    images = GalleryImage.objects.all()
    return render(request, 'gallery.html', {'images': images})

def skills_view(request):
    return render(request, 'skills.html')