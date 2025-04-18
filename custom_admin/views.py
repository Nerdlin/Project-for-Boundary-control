from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from auth_app.models import User
from feedback_app.models import Feedback
from skills.models import UserSkill, SkillCategory
from django import forms
from datetime import datetime

def staff_required(user):
    return user.is_staff

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['is_staff', 'is_superuser']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']

class UserSkillForm(forms.ModelForm):
    class Meta:
        model = UserSkill
        fields = ['skill', 'level']

@user_passes_test(staff_required, login_url='/auth/login/')
def admin_dashboard(request):
    return render(request, 'custom_admin/dashboard.html')

@user_passes_test(staff_required, login_url='/auth/login/')
def user_list(request):
    query = request.GET.get('q', '')
    status_filter = request.GET.get('status', '')

    users = User.objects.all()
    if query:
        users = users.filter(email__icontains=query)
    if status_filter:
        if status_filter == 'admin':
            users = users.filter(is_staff=True)
        elif status_filter == 'regular':
            users = users.filter(is_staff=False)
        elif status_filter == 'superuser':
            users = users.filter(is_superuser=True)

    admin_users = users.filter(is_staff=True)
    regular_users = users.filter(is_staff=False)

    context = {
        'admin_users': admin_users,
        'regular_users': regular_users,
        'query': query,
        'status_filter': status_filter,
    }
    return render(request, 'custom_admin/user_list.html', context)

@user_passes_test(staff_required, login_url='/auth/login/')
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('custom_admin:user_list')
    else:
        form = UserForm(instance=user)
    context = {'form': form, 'user': user}
    return render(request, 'custom_admin/edit_user.html', context)

@user_passes_test(staff_required, login_url='/auth/login/')
def feedback_list(request):
    query = request.GET.get('q', '')
    user_filter = request.GET.get('user', '')
    date_filter = request.GET.get('date', '')

    feedbacks = Feedback.objects.all().select_related('user')
    if query:
        feedbacks = feedbacks.filter(Q(name__icontains=query) | Q(email__icontains=query))
    if user_filter:
        feedbacks = feedbacks.filter(user__id=user_filter)
    if date_filter:
        try:
            date = datetime.strptime(date_filter, '%Y-%m-%d').date()
            feedbacks = feedbacks.filter(created_at__date=date)
        except ValueError:
            pass

    users = User.objects.all()
    context = {
        'feedbacks': feedbacks,
        'users': users,
        'query': query,
        'user_filter': user_filter,
        'date_filter': date_filter,
    }
    return render(request, 'custom_admin/feedback_list.html', context)

@user_passes_test(staff_required, login_url='/auth/login/')
def edit_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            return redirect('custom_admin:feedback_list')
    else:
        form = FeedbackForm(instance=feedback)
    context = {'form': form, 'feedback': feedback}
    return render(request, 'custom_admin/edit_feedback.html', context)

@user_passes_test(staff_required, login_url='/auth/login/')
def skills_list(request):
    query = request.GET.get('q', '')
    user_filter = request.GET.get('user', '')
    skill_filter = request.GET.get('skill', '')
    level_filter = request.GET.get('level', '')

    skills = UserSkill.objects.all().select_related('user', 'skill')
    if query:
        skills = skills.filter(user__username__icontains=query)
    if user_filter:
        skills = skills.filter(user__id=user_filter)
    if skill_filter:
        skills = skills.filter(skill__id=skill_filter)
    if level_filter:
        skills = skills.filter(level=level_filter)

    users = User.objects.all()
    skill_categories = SkillCategory.objects.all()
    level_choices = UserSkill.LEVEL_CHOICES

    context = {
        'skills': skills,
        'users': users,
        'skill_categories': skill_categories,
        'level_choices': level_choices,
        'query': query,
        'user_filter': user_filter,
        'skill_filter': skill_filter,
        'level_filter': level_filter,
    }
    return render(request, 'custom_admin/skills_list.html', context)

@user_passes_test(staff_required, login_url='/auth/login/')
def edit_skill(request, skill_id):
    skill = get_object_or_404(UserSkill, id=skill_id)
    if request.method == 'POST':
        form = UserSkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('custom_admin:skills_list')
    else:
        form = UserSkillForm(instance=skill)
    context = {'form': form, 'skill': skill}
    return render(request, 'custom_admin/edit_skill.html', context)