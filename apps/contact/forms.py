# -*- coding: utf-8 -*-
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Div, MultiField
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

from django import forms
from django.utils.translation import ugettext_lazy as _
from captcha.fields import ReCaptchaField


class ContactForm(forms.Form):
    name = forms.CharField(label=_('Name'), max_length=100, required=True,
                           widget=forms.TextInput())
    email_or_phone = forms.CharField(label=_('Email or phone '), max_length=200, required=True,
                                     widget=forms.TextInput())
    message = forms.CharField(label=_('Message'), max_length=255,
                              widget=forms.Textarea(), required=True)
    captcha = ReCaptchaField()

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = '.'
        self.help_text_inline = True
        self.html5_required = True
        self.helper.layout = Layout(
            Div(
                Div('name', css_class="col-md-6 form-group"),
                Div('email_or_phone', css_class="col-md-6 form-group col-sm-12"),
                Div('message', css_class="form-group col-md-12"),
                Div('captcha', css_class="form-group col-md-6 col-sm-12"),
                css_class='row')
        )
        super(ContactForm, self).__init__(*args, **kwargs)
