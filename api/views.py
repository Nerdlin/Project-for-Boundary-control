from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import GalleryImageSerializer
from pages_app.models import GalleryImage

class GalleryImageViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer

