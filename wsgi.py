import os,sys
sys.path.append('/home/lee/')
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ap.settings")

os.environ['DJANGO_SETTINGS_MODULE'] = "ap.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
