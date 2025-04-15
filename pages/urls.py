from django.urls import path
from .views import index_view, history_view, features_view, gallery_view, skills_view

urlpatterns = [
    path('', index_view, name='index'),
    path('history/', history_view, name='history'),
    path('features/', features_view, name='features'),
    path('gallery/', gallery_view, name='gallery'),
    path('skills/', skills_view, name='skills'),
]