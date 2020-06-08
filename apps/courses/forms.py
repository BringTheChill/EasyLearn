from django import forms
from django.contrib.auth import password_validation

from .models import Course, Section
from .widgets import DropzoneFileInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.utils.translation import gettext, gettext_lazy as _

# START
from .models import Student
from users.models import CustomUser
from users.forms import CustomUserCreationForm


class StudentSignUpForm(CustomUserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control formWidth', }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control formWidth', }),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta(CustomUserCreationForm.Meta):
        model = CustomUser
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        widgets = {'email': forms.EmailInput(attrs={'class': 'form-control formWidth', }),
                   # 'password1': forms.TextInput(attrs={'class': 'form-control formWidth test', }),
                   # 'password2': forms.TextInput(attrs={'class': 'form-control formWidth test', }),
                   'first_name': forms.TextInput(attrs={'class': 'form-control formWidth', }),
                   'last_name': forms.TextInput(attrs={'class': 'form-control formWidth', }),
                   }

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        Student.objects.create(user=user)


class TeacherSignUpForm(CustomUserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control formWidth', }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control formWidth', }),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta(CustomUserCreationForm.Meta):
        model = CustomUser
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        widgets = {'email': forms.EmailInput(attrs={'class': 'form-control formWidth', }),
                   'password1': forms.PasswordInput(attrs={'class': 'form-control formWidth', }),
                   'password2': forms.PasswordInput(attrs={'class': 'form-control formWidth', }),
                   'first_name': forms.TextInput(attrs={'class': 'form-control formWidth', }),
                   'last_name': forms.TextInput(attrs={'class': 'form-control formWidth', }),
                   }

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
