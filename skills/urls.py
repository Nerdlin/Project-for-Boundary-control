from django.urls import path
from . import views

app_name = 'skills'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('edit_skill/<int:skill_id>/', views.edit_skill, name='edit_skill'),
    path('delete_skill/<int:skill_id>/', views.delete_skill, name='delete_skill'),
    path('delete_all_skills/', views.delete_all_skills, name='delete_all_skills'),
]