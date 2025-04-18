"""
URL configuration for datascience_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

