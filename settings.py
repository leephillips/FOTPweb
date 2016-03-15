# Django settings for ap project.

DEBUG = True
# DEBUG = False
# TEMPLATE_DEBUG = True
TEMPLATE_DEBUG = False
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SESSION_COOKIE_AGE = 365*24*60*60

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        # Values below are imported from secret_settings.py 
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


SITE_ID = 7

ADMINS = (
     (), #imported from secret_settings.py
)

ADMINURL = '/admin/'

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

ALLOWED_HOSTS = ['*']

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True
USE_I18N = False
USE_TZ = False

# Make this unique, and don't share it with anybody.
SECRET_KEY = '' # imported from secret_settings.py

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
  'django.contrib.messages.context_processors.messages',
  'django.contrib.auth.context_processors.auth',
  'django.core.context_processors.request',
  'ap.context_processors.media',
  'ap.context_processors.static',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'ap.urls'

WSGI_APPLICATION = 'ap.wsgi.application'

TEMPLATE_DIRS = (
    "/home/lee/ap/templates",
)

TINYMCE_DEFAULT_CONFIG =   {'theme': 'advanced', 'relative_urls': False}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # 'django.contrib.staticfiles',
    'django.contrib.admin',
    # 'django.contrib.sites',
    # 'django.contrib.admin.apps.SimpleAdminConfig',
    'ap.apdirposts',
    'ap.boarddocs',
    'todo',
)

ALLOWED_INCLUDE_ROOTS = ('/home/lee/www/arlplanet',)

AUTH_PROFILE_MODULE = 'apdirposts.Director'

STATIC_ROOT = '/home/lee/ap/static'
STATIC_URL = '/static/'
MEDIA_ROOT = '/home/lee/ap/media/'
MEDIA_URL = '/media/'

from secret_settings import *
