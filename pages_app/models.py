from django.db import models

from auth_app.models import User


class GalleryImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gallery_images', null=True)
    image = models.ImageField(upload_to='gallery/')  # Изображения будут сохраняться в media/gallery/
    alt_text = models.CharField(max_length=255, blank=True)  # Альтернативный текст (необязательный)

    def __str__(self):
        return self.alt_text or "Изображение"


