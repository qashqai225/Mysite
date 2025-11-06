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

def home(request):
    data = {
        'news': news,
        'title': 'Наша головна сторінка'
    }
    return render(request, 'blog/home.html', data)
def contaktu(request):
    return render(request, 'blog/contaktu.html')
def main_menu(request):
    return render(request, 'blog/main_menu.html')