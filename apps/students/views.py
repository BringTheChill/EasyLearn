from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from rest_framework import viewsets

from users.forms import CustomUserCreationForm

from courses.models import Course
from courses.views import calculate_score
from users.models import CustomUser
from .serializers import UserSerializer
from django.contrib import messages


def get_all_scores_for_user(user):
    scores = []
    for course in Course.objects.all():
        course_scores = []
        for section in course.section_set.order_by('number'):
            course_scores.append((section, calculate_score(user, section),))
        scores.append((course, course_scores), )
    return scores


def student_detail(request):
    if not request.user.is_authenticated:
        raise PermissionDenied
    student = request.user
    return render(request, 'students/student_detail.html',
                  {'student': student, 'scores': get_all_scores_for_user(student)})


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.order_by('-date_joined')
    serializer_class = UserSerializer

