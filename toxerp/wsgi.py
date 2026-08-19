"""
Django WSGI application entry point for Railway, Heroku, and gunicorn.
This file is required by Railway's Nixpacks builder.
"""
import os
from django.core.wsgi import get_wsgi_application

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'toxerp.settings')

# Get the WSGI application
application = get_wsgi_application()
