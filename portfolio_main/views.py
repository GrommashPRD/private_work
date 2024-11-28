from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string

from portfolio_main.models import Works

# Create your views here.

menu = [{'title': 'Обо мне', 'url_name': 'about'},
        {'title': 'Работы', 'url_name': 'works'},
        {'title': 'Контакты', 'url_name': 'contacts'}]


def index(request):
    posts = Works.objects.all()
    data = {
        'title': 'Домашняя страница',
        'menu': menu,
        'posts': posts,
    }
    return render(request, 'portfolio_main/index.html', context=data)


def contacts(request):
    return render(request, 'portfolio_main/contacts.html',
                  {'title': 'Мои контакты:', 'menu': menu}
                  )


def about_me(request):
    return render(request, 'portfolio_main/about_me.html',
                  {'title': 'Обо мне:', 'menu': menu}
                  )


def works(request):
    posts = Works.objects.all()
    return render(request, 'portfolio_main/works.html',
                  {'title': 'Мои работы:', 'menu': menu, 'posts': posts}
                  )

def page_404(request, exception):
    return HttpResponseNotFound('Страинца не найдена 404')
