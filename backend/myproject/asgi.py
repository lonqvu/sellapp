"""
ASGI config for myproject project.
"""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings.prod')

application = get_asgi_application() 