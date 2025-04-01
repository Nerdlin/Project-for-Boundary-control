# Create your models here.
from django.db import models

class GalleryImage(models.Model):
    image = models.ImageField(upload_to="img/")
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

