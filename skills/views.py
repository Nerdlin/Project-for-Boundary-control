from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserSkill, SkillCategory
from .forms import UserSkillForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib.parse import urlencode
from django.urls import reverse

@login_required
def profile(request):
    # Получаем параметры фильтрации и пагинации из GET-запроса
    query = request.GET.get('q', '').strip().lower()  # Удаляем пробелы и приводим к нижнему регистру
    level_filter = request.GET.get('level', '')
    page = request.GET.get('page', 1)

    # Получаем навыки текущего пользователя
    user_skills = UserSkill.objects.filter(user=request.user)

    # Применяем фильтрацию
    if query:
        user_skills = user_skills.filter(skill__name__icontains=query)
        # Добавляем отладочное сообщение, чтобы понять, сколько навыков найдено
        print(f"Поиск по запросу '{query}': найдено {user_skills.count()} навыков")
    if level_filter:
        user_skills = user_skills.filter(level=level_filter)

    # Пагинация: 5 навыков на страницу
    paginator = Paginator(user_skills, 5)
    try:
        user_skills_page = paginator.page(page)
    except PageNotAnInteger:
        user_skills_page = paginator.page(1)
    except EmptyPage:
        user_skills_page = paginator.page(paginator.num_pages)

    # Обработка формы добавления навыка
    if request.method == 'POST':
        form = UserSkillForm(request.POST)
        if form.is_valid():
            skill = form.cleaned_data['skill']
            if UserSkill.objects.filter(user=request.user, skill=skill).exists():
                form.add_error('skill', 'Этот навык уже добавлен.')
            else:
                user_skill = form.save(commit=False)
                user_skill.user = request.user
                user_skill.profile = request.user.profile
                print(f"Сохраняем навык: {user_skill.skill.name}, уровень: {user_skill.level}")
                try:
                    user_skill.save()
                    messages.success(request, f'Навык "{user_skill.skill.name}" успешно добавлен.')
                except Exception as e:
                    print(f"Ошибка сохранения навыка: {e}")
                    form.add_error(None, 'Ошибка сохранения навыка. Попробуйте снова.')
                    return render(request, 'skills/profile.html', {
                        'form': form,
                        'user_skills': user_skills_page,
                        'query': query,
                        'level_filter': level_filter,
                    })
                redirect_url = reverse('skills:profile')
                if request.GET:
                    redirect_url += f"?{request.GET.urlencode()}"
                return redirect(redirect_url)
        else:
            print("Форма недействительна:", form.errors)
    else:
        form = UserSkillForm()

    return render(request, 'skills/profile.html', {
        'form': form,
        'user_skills': user_skills_page,
        'query': query,
        'level_filter': level_filter,
        'level_choices': UserSkill.LEVEL_CHOICES,
    })

@login_required
def edit_skill(request, skill_id):
    user_skill = get_object_or_404(UserSkill, id=skill_id, user=request.user)
    if request.method == 'POST':
        form = UserSkillForm(request.POST, instance=user_skill)
        if form.is_valid():
            form.save()
            messages.success(request, f'Навык "{user_skill.skill.name}" успешно обновлен.')
            return redirect('skills:profile')
    else:
        form = UserSkillForm(instance=user_skill)
    return render(request, 'skills/edit_skill.html', {'form': form, 'user_skill': user_skill})

@login_required
def delete_skill(request, skill_id):
    user_skill = get_object_or_404(UserSkill, id=skill_id, user=request.user)
    if request.method == 'POST':
        skill_name = user_skill.skill.name
        user_skill.delete()
        messages.success(request, f'Навык "{skill_name}" успешно удален.')
        return redirect('skills:profile')
    return render(request, 'skills/confirm_delete.html', {'user_skill': user_skill})

@login_required
def delete_all_skills(request):
    if request.method == 'POST':
        UserSkill.objects.filter(user=request.user).delete()
        messages.success(request, 'Все навыки успешно удалены.')
        return redirect('skills:profile')
    return render(request, 'skills/confirm_delete_all.html')