from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    form = UserCreationForm()
    
    return render(request, 'users/register.html', {'form': form, 'title': 'Реєстрація користувача'})