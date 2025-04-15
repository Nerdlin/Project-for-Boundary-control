# Create your models here.
from django.db import models

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')  # Изображения будут сохраняться в media/gallery/
    title = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title

