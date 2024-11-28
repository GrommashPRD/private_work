from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about_me, name='about'),
    path('contact/', views.contacts, name='contacts'),
    path('works/', views.works, name='works'),
]