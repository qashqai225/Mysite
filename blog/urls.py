from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('contaktu/', views.contaktu, name='blog-contaktu'),
]
