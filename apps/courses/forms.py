from django import forms
from .models import Course
from .widgets import DropzoneFileInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'price', 'category', 'file']
        widgets = {'file': forms.FileInput(
            attrs={'style': 'display: none;', 'class': 'form-control formSpace', 'required': False, }
        )}

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
                Div('name'),
                Div('price'),
                Div('category'),
                Div('file', css_class="mt-5"),
        )
