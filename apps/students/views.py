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
    # parcurgem doar cursurile in care studentul este inscris
    for course in Course.objects.filter(students=user):
        course_scores = []
        for section in course.section_set.order_by('number'):
            course_scores.append((section, calculate_score(user, section),))
        scores.append((course, course_scores), )
    return scores


def get_all_scores_for_teacher(teacher):
    scores = []
    # parcurgem doar cursurile in care studentul este inscris
    for course in Course.objects.filter(teachers=teacher):
        course_scores = []
        for section in course.section_set.order_by('number'):
            for student in course.students.all():
                course_scores.append((student, section, calculate_score(student, section),))
        scores.append((course, course_scores), )
    return scores


def student_detail(request):
    if not request.user.is_authenticated:
        raise PermissionDenied
    if request.user.is_student is True:
        student = request.user
        return render(request, 'students/student_detail.html',
                      {'student': student, 'scores': get_all_scores_for_user(student)})
    if request.user.is_teacher is True:
        teacher = request.user
        return render(request, 'teachers/teacher_detail.html',
                      {'teacher': teacher, 'scores': get_all_scores_for_teacher(teacher)})


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.order_by('-date_joined')
    serializer_class = UserSerializer
