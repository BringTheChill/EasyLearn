from django.core.exceptions import PermissionDenied, SuspiciousOperation
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Course, Section, UserAnswer, Question
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


def do_section(request, section_id):
    section = Section.objects.get(id=section_id)
    return render(request, 'courses/do_section.html', {'section': section})


# def do_section(request):
#     if not request.user.is_authenticated:
#         raise PermissionDenied
#     section = request.user
#     return render(request, 'courses/do_section.html', {'section': section})


def do_test(request, section_id):
    if not request.user.is_authenticated:
        raise PermissionDenied
    section = Section.objects.get(id=section_id)
    if request.method == 'POST':
        # in caz de ceva e gresit mai jos nu salveaza
        with transaction.atomic():
            # stergem toate raspunsurile anterioare in caz de se da testul din nou
            UserAnswer.objects.filter(user=request.user, question__section=section).delete()
            for key, value in request.POST.items():
                if key == 'csrfmiddlewaretoken':
                    continue
                # {'question-1': '2'}
                question_id = key.split('-')[1]
                question = Question.objects.get(id=question_id)
                answer_id = int(request.POST.get(key))
                if answer_id not in question.answer_set.values_list('id', flat=True):
                    raise SuspiciousOperation('Answer is not valid for this question')
                user_answer = UserAnswer.objects.create(user=request.user, question=question, answer_id=answer_id, )
        return redirect(reverse('show_results', args=(section_id,)))
    return render(request, 'courses/do_test.html', {'section': section})


def calculate_score(user, section):
    questions = Question.objects.filter(section=section)
    correct_answers = UserAnswer.objects.filter(user=user, question__section=section, answer__correct=True)
    return (correct_answers.count() / questions.count()) * 100


def show_results(request, section_id):
    if not request.user.is_authenticated:
        raise PermissionDenied
    section = Section.objects.get(id=section_id)
    return render(request, 'courses/show_results.html', {'section': section, 'score': calculate_score(request.user,
                                                                                                      section)})
