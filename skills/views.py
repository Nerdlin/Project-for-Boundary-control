from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserSkill, SkillCategory
from .forms import UserSkillForm


@login_required
def profile(request):
    # Получаем навыки текущего пользователя
    user_skills = UserSkill.objects.filter(user=request.user)

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
                print(f"Сохраняем навык: {user_skill.skill.name}, уровень: {user_skill.level}")  # Отладочное сообщение
                try:
                    user_skill.save()
                    messages.success(request, f'Навык "{user_skill.skill.name}" успешно добавлен.')
                except Exception as e:
                    print(f"Ошибка сохранения навыка: {e}")  # Логируем ошибку
                    form.add_error(None, 'Ошибка сохранения навыка. Попробуйте снова.')
                    return render(request, 'skills/profile.html', {
                        'form': form,
                        'user_skills': user_skills,
                    })
                return redirect('profile')
        else:
            print("Форма недействительна:", form.errors)  # Отладочное сообщение
    else:
        form = UserSkillForm()

    # Передаем данные в шаблон
    return render(request, 'skills/profile.html', {
        'form': form,
        'user_skills': user_skills,
    })


@login_required
def edit_skill(request, skill_id):
    user_skill = get_object_or_404(UserSkill, id=skill_id, user=request.user)

    if request.method == 'POST':
        form = UserSkillForm(request.POST, instance=user_skill)
        if form.is_valid():
            form.save()
            messages.success(request, f'Навык "{user_skill.skill.name}" успешно обновлен.')
            return redirect('profile')
    else:
        form = UserSkillForm(instance=user_skill)

    return render(request, 'skills/edit_skill.html', {'form': form, 'user_skill': user_skill})


@login_required
def delete_skill(request, skill_id):
    user_skill = get_object_or_404(UserSkill, id=skill_id, user=request.user)
    if request.method == 'POST':
        skill_name = user_skill.skill.name  # Сохраняем имя навыка перед удалением
        user_skill.delete()
        messages.success(request, f'Навык "{skill_name}" успешно удален.')
        return redirect('profile')
    return render(request, 'skills/confirm_delete.html', {'user_skill': user_skill})


@login_required
def delete_all_skills(request):
    if request.method == 'POST':
        UserSkill.objects.filter(user=request.user).delete()
        messages.success(request, 'Все навыки успешно удалены.')
        return redirect('profile')
    return render(request, 'skills/confirm_delete_all.html')