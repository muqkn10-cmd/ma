"""
Django settings for toxerp project.
Built on Django 4.2 for a local-first, loopback-only ERP system for Iraqi small businesses.
"""

import os
from pathlib import Path

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'dev-only-insecure-key')

# SECURITY WARNING: don't run with debug turned on in production!
# Explicit behaviour: DEBUG must be set to '1' to enable debug mode in production
DEBUG = os.environ.get('TOX_DEBUG', '0') == '1'

# ALLOWED_HOSTS can be configured via TOX_ALLOWED_HOSTS or ALLOWED_HOSTS env var
# Default includes the current Railway hostname and a wildcard for *.up.railway.app
_raw_hosts = os.environ.get('TOX_ALLOWED_HOSTS') or os.environ.get('ALLOWED_HOSTS')
if _raw_hosts:
    ALLOWED_HOSTS = [h.strip() for h in _raw_hosts.split(',') if h.strip()]
else:
    ALLOWED_HOSTS = [
        'moq.up.railway.app',  # this project's Railway public domain
        'web-production-181d1.up.railway.app',
        'localhost',
        '127.0.0.1',
        '.up.railway.app',  # allow Railway subdomains
    ]

# When behind a proxy (Railway, Heroku, etc.) the forwarded proto/header should be respected
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# This is the key setting that Railway's Nixpacks requires!
WSGI_APPLICATION = 'toxerp.wsgi.application'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party
    'rest_framework',
    # Local apps
    'erp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Static files for Railway
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'toxerp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Include repo templates directory and repository root so index.html/pages are found
        'DIRS': [BASE_DIR / 'templates', BASE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Database
# - Default: SQLite (local / desktop mode).
# - Production: if DATABASE_URL is set (Railway/Postgres), use PostgreSQL so
#   data persists across restarts/deploys (Railway's filesystem is ephemeral).
_database_url = os.environ.get('DATABASE_URL')
if _database_url:
    import urllib.parse as _urlparse

    _db = _urlparse.urlparse(_database_url)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': _db.path.lstrip('/'),
            'USER': _db.username,
            'PASSWORD': _db.password,
            'HOST': _db.hostname,
            'PORT': _db.port or 5432,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization - Set to Arabic
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Baghdad'
USE_I18N = True
USE_TZ = True

# Static files
# Serve static files under /static/ so they don't conflict with the root URL
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
# Collect static from assets/ so paths like /static/assets/... resolve.
# The "assets" prefix preserves the directory level so the collected files keep
# the /assets/... path that the templates reference (a bare path here would
# strip the prefix and collect them as /static/css/..., causing 404s).
STATICFILES_DIRS = [
    ('assets', BASE_DIR / 'assets'),
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST Framework configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[{levelname}] {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '[{levelname}] {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
