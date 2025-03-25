from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from datascience_project.pages_app.models import GalleryImage
from .serializers import GalleryImageSerializer

class GalleryImageViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer