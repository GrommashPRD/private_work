from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string


# Create your views here.

menu = [
    "Контакты",
    "Обо мне",
    "Работы",
]


def index(request):
    data = {
        'title': 'Домашняя страница',
        'menu': menu,
    }
    return render(request, 'portfolio_main/index.html', context=data)


def contacts(request):
    return render(request, 'portfolio_main/contacts.html', {'title': 'Мои контакты:'})


def about_me(request):
    return HttpResponse("Hello, about me.")


def works(request):
    return HttpResponse("Hello, works.")


def page_404(request, exception):
    return HttpResponseNotFound('Страинца не найдена 404')
