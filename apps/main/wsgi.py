import os
from os.path import dirname, abspath
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

APP_ROOT = dirname(abspath(__file__))

load_dotenv(os.path.join(APP_ROOT, '.env'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

application = get_wsgi_application()
