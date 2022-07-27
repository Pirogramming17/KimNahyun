
from django.contrib import admin
from django.urls import path
from . import views

app_name='posts'

urlpatterns = [
    path('', views.main, name='main'),
    path('like/', views.like, name='like'),
    path('delete/', views.delete, name='delete'),
]