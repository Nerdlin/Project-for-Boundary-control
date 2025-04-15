from django import forms
from .models import UserSkill, SkillCategory

class UserSkillForm(forms.ModelForm):
    skill = forms.ModelChoiceField(
        queryset=SkillCategory.objects.all(),
        widget=forms.Select(attrs={'class': 'skill-select'}),
        label="Навык"
    )
    level = forms.ChoiceField(
        choices=UserSkill.LEVEL_CHOICES,
        widget=forms.Select(attrs={'class': 'level-select'}),
        label="Уровень владения"
    )

    class Meta:
        model = UserSkill
        fields = ['skill', 'level']