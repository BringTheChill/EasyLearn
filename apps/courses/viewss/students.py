from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.views.generic import CreateView

from ..forms import StudentSignUpForm
# from ..models import User
from users.models import CustomUser


class StudentSignUpView(CreateView):
    model = CustomUser
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        new_user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password1'])
        login(self.request, new_user)
        return redirect('index')
