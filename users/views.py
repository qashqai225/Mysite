from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegForm

def register(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Обліковий запис для {username} створено успішно!')
            return redirect('blog-home')
    else:
        form = UserRegForm()
    
    return render(request, 'users/register.html', {'form': form, 'title': 'Реєстрація користувача'}) 