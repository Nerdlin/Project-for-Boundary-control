from django.db import models
from auth_app.models import User, Profile  # Импорт модели Profile

# Модель для предопределенного списка навыков
class SkillCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Модель для связи пользователя и навыка
class UserSkill(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Новичок'),
        ('intermediate', 'Средний'),
        ('advanced', 'Продвинутый'),
        ('want_to_learn', 'Хочу изучить'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_skills')  # Связь с User
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_skills', null=True, default=None)  # Добавлены null=True и default=None
    skill = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='user_skills')  # Связь с SkillCategory
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='beginner')

    class Meta:
        unique_together = ('user', 'skill')  # Пользователь не может иметь один и тот же навык дважды

    def __str__(self):
        return f"{self.user.username} - {self.skill.name} ({self.level})"