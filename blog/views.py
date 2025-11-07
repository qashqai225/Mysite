from django.shortcuts import render
from django.http import HttpResponse

news = [
    {
        'title': '1 news',
        'text': 'abra kadabra',
        'date': '1 yanuara 2025',
        'avtor': 'Greg'
    },
    {
        'title': '2 news',
        'text': 'abra kadabra',
        'date': '1 september 2025',
        'avtor': 'Yorik'
    }

]

news_contact = [
    {
        'title': 'Перша новина',
        'text': 'Начепто тексту для першої новини',
        'date': '1 yanuara 2025',
        'avtor': 'Навальний'
    },
    {
        'title': 'Друга новина',
        'text': 'Начепто тексту для другої новини',
        'date': '',
        'avtor': 'Зеленський'
    }

]


def home(request):
    data = {
        'news': news,
        'title': 'Наша головна сторінка',        
    }
    return render(request, 'blog/home.html', data)

def contaktu(request):
    data = {
        'news_contact': news_contact,
        'title': 'Контакти MySite',        
    }
    return render(request, 'blog/contaktu.html', data)

