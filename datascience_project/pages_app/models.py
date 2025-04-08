from django.db import models

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')  # Изображения будут сохраняться в media/gallery/
    alt_text = models.CharField(max_length=255, blank=True)  # Альтернативный текст (необязательный)

    def __str__(self):
        return self.alt_text or "Изображение"


