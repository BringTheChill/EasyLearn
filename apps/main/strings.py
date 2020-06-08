from django.utils.translation import ugettext_lazy as _

CONTACT_EMAIL_SUBJECT = _(
    'EasyLearn | Mesaj de la "%(person_name)s"')


CONTACT_EMAIL_BODY = _('''Mesaj de pe site,

Nume: {{ name }}
Email sau telefon: {{ email_or_phone }}
Mesaj: {{ message  }}

Salutari de la robotelul de serviciu al EasyLearn.''')
