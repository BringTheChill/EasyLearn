#!/usr/bin/env python
import os
import sys
from os.path import dirname, abspath
from dotenv import load_dotenv

APP_ROOT = dirname(dirname(abspath(__file__)))

load_dotenv(os.path.join(APP_ROOT, 'apps/main/.env'))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
