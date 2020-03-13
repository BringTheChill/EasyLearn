from django.contrib import admin
from django.urls import path
from .views import index, course_add

urlpatterns = [
    path('course_add/', course_add, name='course_add'),
    path('', index, name='index')
]
