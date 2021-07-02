"""
WSGI config for TodosBackend project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TodosBackend.settings')

application = get_wsgi_application()
application = WhiteNoise(application)