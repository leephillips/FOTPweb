import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'ap.settings'
os.environ['PYTHONPATH'] = '/home/lee:home/lee/converters'
sys.path.append('/home/lee')
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

