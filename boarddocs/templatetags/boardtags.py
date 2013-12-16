import os

from django import template


register = template.Library()

@register.filter
def filename(value):
   try:
       return os.path.basename(value)
   except:
       return value

