from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied, SuspiciousOperation
from django.urls import reverse
from django.db import transaction
from django.views.generic import DetailView, ListView

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Course, Section, UserAnswer, Question
from .forms import CourseForm
from courses.serializers import SectionSerializer


class CourseListView(ListView):
    model = Course
    queryset = Course.objects.prefetch_related('students__students_to_courses')


course_list = CourseListView.as_view()


def course_add(request):
    if request.POST:
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            new_course = form.save()
            return HttpResponseRedirect(new_course.get_absolute_url())
    else:
        form = CourseForm()
    return render(request, 'courses/course_form.html', {'form': form})


class CourseDetailView(DetailView):
    model = Course


course_detail = CourseDetailView.as_view()


def do_section(request, section_id):
    section = Section.objects.get(id=section_id)
    if request.user in section.course.students.all() or request.user is section.course.teachers:
        return render(request, 'courses/do_section.html', {'section': section})
    raise PermissionDenied


def do_test(request, section_id):
    section = Section.objects.get(id=section_id)
    if not request.user.is_authenticated or request.user not in section.course.students.all():
        raise PermissionDenied
    if request.method == 'POST':
        data = {}
        for key, value in request.POST.items():
            if key == 'csrfmiddlewaretoken':
                continue
            # {'question-1': '2'}
            question_id = key.split('-')[1]
            answer_id = request.POST.get(key)
            data[question_id] = answer_id
        perform_test(request.user, data, section)
        return redirect(reverse('show_results', args=(section_id,)))
    return render(request, 'courses/do_test.html', {'section': section})


def perform_test(user, data, section):
    with transaction.atomic():
        UserAnswer.objects.filter(user=user, question__section=section).delete()
        for question_id, answer_id in data.items():
            question = Question.objects.get(id=question_id)
            answer_id = int(answer_id)
            if answer_id not in question.answer_set.values_list('id', flat=True):
                raise SuspiciousOperation('Answer is not valid for this question')
            user_answer = UserAnswer.objects.create(user=user, question=question, answer_id=answer_id)


def calculate_score(user, section):
    questions = Question.objects.filter(section=section)
    correct_answers = UserAnswer.objects.filter(user=user, question__section=section, answer__correct=True)
    try:
        return (correct_answers.count() / questions.count()) * 100
    except ZeroDivisionError:
        return 0


def show_results(request, section_id):
    if not request.user.is_authenticated:
        raise PermissionDenied
    section = Section.objects.get(id=section_id)
    return render(request, 'courses/show_results.html', {'section': section, 'score': calculate_score(request.user,
                                                                                                      section)})


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

    @action(detail=True, methods=['GET', ])
    def questions(self, request, *args, **kwargs):
        section = self.get_object()
        data = []
        for question in section.question_set.all():
            question_data = {'id': question.id, 'answers': []}
            for answer in question.answer_set.all():
                answer_data = {'id': answer.id, 'text': str(answer), }
                question_data['answers'].append(answer_data)
            data.append(question_data)
        return Response(data)


def course_enroll(request, pk):
    course = Course.objects.get(pk=pk)
    if request.user in course.students.all() or request.user is course.teachers:
        message = "Sunteti deja inscris la curs!"
    else:
        course.students.add(request.user)
        message = "Ati fost inscris cu succces!"
    return render(request, "courses/course_enrolled.html", {"message": message})
