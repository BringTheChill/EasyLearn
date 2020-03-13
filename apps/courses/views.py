from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Course
from .forms import CourseForm


def index(request):
    courses = Course.objects.all
    return render(request, "courses.html", {'courses': courses})


def course_add(request):
    if request.POST:
        form = CourseForm(request.POST)
        if form.is_valid():
            new_course = form.save()
            return HttpResponseRedirect('/courses/')
    else:
        form = CourseForm()
    return render(request, 'course_form.html', {
        'form': form,
    })
