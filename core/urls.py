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
from pages_app.views import admin_panel_view  # Импортируем новый view
from pages_app.views import user_details_view

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
    path('auth/password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('auth/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('auth/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('auth/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('admin-panel/', staff_member_required(admin_panel_view), name='admin_panel'),
    path('user/<int:user_id>/', user_details_view, name='user_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

