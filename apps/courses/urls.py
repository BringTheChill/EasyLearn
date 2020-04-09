from django.contrib import admin
from django.urls import path
from .views import index, course_add, course_detail

urlpatterns = [
    path('course_detail/<course_id>', course_detail, name='course_detail'),
    path('course_add/', course_add, name='course_add'),
    path('', index, name='index')
]
