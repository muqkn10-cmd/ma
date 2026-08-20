"""
Django WSGI application entry point for Railway, Heroku, and gunicorn.
This file is required by Railway's Nixpacks builder.
"""
import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'toxerp.settings')

# Get the WSGI application
application = get_wsgi_application()

# Wrap the application with WhiteNoise at the WSGI level for robust
# static file serving from Gunicorn on Railway.
application = WhiteNoise(application, root='/app/staticfiles')
