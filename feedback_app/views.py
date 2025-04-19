from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)  # Не сохраняем сразу в базу
            if request.user.is_authenticated:  # Если пользователь авторизован
                feedback.user = request.user   # Привязываем пользователя
            feedback.save()  # Теперь сохраняем
            return redirect('index')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})