"""
URL configuration for datascience_project project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django.contrib.admin.views.decorators import staff_member_required

from api_app.views import GalleryImageViewSet

router = DefaultRouter()
router.register(r'gallery', GalleryImageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages_app.urls')),
    path('auth/', include('auth_app.urls')),
    path('feedback/', include('feedback_app.urls')),
    path('api/', include(router.urls)),
    path('user/', include('skills.urls')),
    path('admin-panel/', include('custom_admin.urls', namespace='custom_admin')),
]

# Добавляем маршруты для медиафайлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)