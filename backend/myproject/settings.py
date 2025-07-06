"""
Django settings for myproject.
"""
import os

# Set the Django settings module based on environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings.dev')

# Import the appropriate settings
from .settings.dev import * 