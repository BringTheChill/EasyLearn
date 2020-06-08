from django.shortcuts import render
from django.views.generic import ListView

from courses.models import Course


def index(request):
    return render(request, 'index.html', {})