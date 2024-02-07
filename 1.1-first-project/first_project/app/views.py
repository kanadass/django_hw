from datetime import datetime
from os import listdir

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    template_name = 'app/time.html'
    current_time = datetime.now().time().isoformat(timespec='seconds')
    home = reverse('home')
    context = {
        "home": home,
        "current_time": current_time,
    }
    # msg = f'Текущее время: {current_time}'
    return render(request, template_name, context)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей
    # директории
    template_name = 'app/lstdir.html'
    home = reverse('home')
    # lst_dir = ', '.join(listdir(path='.'))
    lst_dir = listdir(path='.')
    context = {
        "home": home,
        "lst_dir": lst_dir,
    }

    # msg = f'Список текущей директории: {lst_dir}'
    # return HttpResponse(msg)
    return render(request, template_name, context)
