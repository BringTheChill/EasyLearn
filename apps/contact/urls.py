from django.conf.urls import url
from .views import index, api_contact_send

urlpatterns = [
    url('^api_contact_send', api_contact_send, name='api_contact_send'),
    url('^', index, name='contact_view'),
]
