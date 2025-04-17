from django.db import models
from django.conf import settings

from auth_app.models import User


class GalleryImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gallery_images', null=True)
    image = models.ImageField(upload_to='gallery/')  # Изображения будут сохраняться в media/gallery/
    alt_text = models.CharField(max_length=255, blank=True)  # Альтернативный текст (необязательный)

    def __str__(self):
        return self.alt_text or "Изображение"

class Feedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pages_app_feedbacks')


