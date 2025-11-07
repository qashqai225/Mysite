from django.shortcuts import render
from .models import News



text_contact = [
    {
        'title': 'Наші контакти',
        'text': 'вул. Поштова 12, м. Київ, Україна. Індекс 01001',
        'avtor': 'Yorik Petrovich',
        'email': 'harleyDavitson@gmail.com',
        'phone': '+380671234567'
    },
    
]


def home(request):
    data = {
        'news': News.objects.all(),
        'title': 'Наша головна сторінка',        
    }
    return render(request, 'blog/home.html', data)

def contaktu(request):
    data = {
        'text_contact': text_contact,
        'title': 'Контакти MySite',        
    }
    return render(request, 'blog/contaktu.html', data)

