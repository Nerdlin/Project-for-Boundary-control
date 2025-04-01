from django.db import models

# Create your models here.
from django.db import models

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='img/')
    alt_text = models.CharField(max_length=255)

