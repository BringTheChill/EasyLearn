from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.base import Context, Template
from django.conf import settings
from django.utils.encoding import force_text

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from constance import config

from main import strings
from .forms import ContactForm


def index(request):
    if request.is_ajax() or request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            email_to = config.EMAIL
            email_from = settings.DEFAULT_FROM_EMAIL
            message = contact_form.cleaned_data['message']
            name = contact_form.cleaned_data['name']
            email_or_phone = contact_form.cleaned_data['email_or_phone']
            email_subject = force_text(strings.CONTACT_EMAIL_SUBJECT % {'person_name': name})
            email = EmailMultiAlternatives(email_subject,
                                           Template(strings.CONTACT_EMAIL_BODY).render(Context({

                                               'name': name,
                                               'email_or_phone': email_or_phone,
                                               'message': message,
                                           })), email_from, [email_to], None, None, None, None, None, None)
            email.send()
            return render(request, 'contact/contact_response.html', {})
        else:
            return render(request, 'contact/contact.html', {'contact_form': contact_form})
    f = ContactForm()
    return render(request, 'contact/contact.html', {'contact_form': f})


@api_view(['POST'])
@permission_classes([AllowAny])
def api_contact_send(request):
    if request.is_ajax() or request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            email_to = config.EMAIL
            email_from = settings.DEFAULT_FROM_EMAIL
            message = contact_form.cleaned_data['message']
            name = contact_form.cleaned_data['name']
            email_or_phone = contact_form.cleaned_data['email_or_phone']
            email_subject = force_text(strings.CONTACT_EMAIL_SUBJECT % {'person_name': name})
            email = EmailMultiAlternatives(email_subject,
                                           Template(strings.CONTACT_EMAIL_BODY).render(Context({
                                               'name': name,
                                               'email': email_or_phone,
                                               'message': message,
                                           })), email_from, [email_to], None, None, None, None, None, None)
            email.send()
            return render(request, 'contact/contact_response.html', {})
        else:
            return render(request, 'contact/contact.html', {'contact_form': contact_form})
