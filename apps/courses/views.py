from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Course
from .forms import CourseForm


def index(request):
    courses = Course.objects.prefetch_related('students')
    return render(request, "courses.html", {'courses': courses})


def course_add(request):
    if request.POST:
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            new_course = form.save()
            return HttpResponseRedirect(new_course.get_absolute_url())
    else:
        form = CourseForm()
    return render(request, 'course_form.html', {'form': form})


def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'course_detail.html', {'course': course})
