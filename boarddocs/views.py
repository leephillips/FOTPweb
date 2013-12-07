from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, get_object_or_404
from models import Minutes, Agenda, Annualreport
from datetime import datetime, timedelta
import re
from ap.settings import ADMINURL

today = datetime.now()

def loginrequired(f):
   """Decoration to secure views against non-logged-in users."""
   def securedf(request, *args, **kwargs):
      if request.user.is_authenticated():
         return f(request, *args, **kwargs)
      else:
         return HttpResponseRedirect(ADMINURL)
   return securedf
      
@loginrequired
def minutetop(request):
      n = Minutes.objects.all()
      return render(request, 'boarddocs/minutetop.html', 
                                {'p': n, })

@loginrequired
def start(request):
   return render(request, 'boarddocs/start.html')


