from django import forms
from .models import Course, Section
from .widgets import DropzoneFileInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
# START
from .models import Student
from users.models import CustomUser
from users.forms import CustomUserCreationForm


class StudentSignUpForm(CustomUserCreationForm):

    class Meta(CustomUserCreationForm.Meta):
        model = CustomUser
        fields = ["email", "password1", "password2", "first_name", "last_name"]

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        Student.objects.create(user=user)


class TeacherSignUpForm(CustomUserCreationForm):
    class Meta(CustomUserCreationForm.Meta):
        model = CustomUser
        fields = ["email", "password1", "password2", "first_name", "last_name"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
# END


class VideoForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ["video"]


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'category', 'file']
        widgets = {'file': forms.FileInput(
            attrs={'style': 'display: none;', 'class': 'form-control formSpace', 'required': False, }
        )}

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
                Div('name'),
                # Div('price'),
                Div('category'),
                Div('file', css_class="mt-5"),
        )
