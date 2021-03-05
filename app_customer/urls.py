from django.contrib import admin
from django.urls import path
from .views import create, index

urlpatterns = [
    path('', index),
    path('add', create),
]
