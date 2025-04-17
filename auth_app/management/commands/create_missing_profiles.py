from django.core.management.base import BaseCommand
from auth_app.models import User, Profile

class Command(BaseCommand):
    help = 'Создает отсутствующие профили для пользователей'

    def handle(self, *args, **kwargs):
        users_without_profiles = User.objects.filter(profile__isnull=True)
        for user in users_without_profiles:
            Profile.objects.create(user=user)
            self.stdout.write(self.style.SUCCESS(f'Профиль создан для пользователя {user.username}'))
        self.stdout.write(self.style.SUCCESS('Все отсутствующие профили созданы.'))
