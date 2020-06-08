from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth import authenticate

from ..forms import TeacherSignUpForm
# from ..models import User
from users.models import CustomUser


class TeacherSignUpView(CreateView):
    model = CustomUser
    form_class = TeacherSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.is_staff = True
        # user = form.save(self)
        # response = super(TeacherSignUpView).form_valid(form)
        # response = super().form_valid(form)
        # self.object.groups.add(teacher_group)
        # form.instance.groups.add(teacher_group)
        # user_auth = authenticate(username=user.email, password=form.cleaned_data['password1'])
        # login(self.request, user)
        # return response
        # return redirect('index')
        user = form.save()
        teacher_group = Group.objects.get(name='Teacher')
        form.instance.groups.add(teacher_group)
        new_user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password1'])
        login(self.request, new_user)
        return redirect('index')

