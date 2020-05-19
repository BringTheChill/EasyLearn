from django.contrib import admin
from django.urls import path
from .views import course_list, course_add, course_detail, do_section, do_test, show_results, course_enroll

urlpatterns = [
    path('course/<pk>/', course_detail, name='course_detail'),
    path('course/<pk>/enroll/', course_enroll, name='course_enroll'),
    path('courses/add/', course_add, name='course_add'),
    path('section/<section_id>', do_section, name='do_section'),
    path('section/<section_id>/test/', do_test, name='do_test'),
    path('section/<section_id>/results/', show_results, name='show_results'),
    path('', course_list, name='index')
]
