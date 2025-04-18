from django.urls import path
from . import views

app_name = 'custom_admin'

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('users/', views.user_list, name='user_list'),
    path('users/edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('feedback/', views.feedback_list, name='feedback_list'),
    path('feedback/edit/<int:feedback_id>/', views.edit_feedback, name='edit_feedback'),
    path('skills/', views.skills_list, name='skills_list'),
    path('skills/edit/<int:skill_id>/', views.edit_skill, name='edit_skill'),
]