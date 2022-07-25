from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts,'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'Главная страница'})

def categories(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}")

def pageNotFound(request, exception):
	return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def archive(request, year):
    if int(year) > 3000:
        raise Http404()
        """ниже ПОСТОЯННОЕ перемещение страницы"""
    elif 2022 < int(year) <= 3000:
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Архив по годам</h1>{year}</p>")