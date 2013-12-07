from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, get_object_or_404
from models import Minutes, Agenda, Annualreport, Boardfile, Budgetreport, LegalDoc, Historical, Picture
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
def start(request):
   n = Annualreport.objects.all()
   return render(request, 'boarddocs/start.html', {'p': n, })

@loginrequired
def minutetop(request):
      n = Minutes.objects.all()
      return render(request, 'boarddocs/minutetop.html', {'p': n, })

@loginrequired
def otherfilestop(request):
      n = Boardfile.objects.all()
      return render(request, 'boarddocs/otherfilestop.html', {'p': n, })

@loginrequired
def budgettop(request):
      n = Budgetreport.objects.all()
      return render(request, 'boarddocs/budgettop.html', {'p': n, })

@loginrequired
def agendatop(request):
      n = Agenda.objects.all()
      return render(request, 'boarddocs/agendatop.html', {'p': n, })

@loginrequired
def legaltop(request):
      n = LegalDoc.objects.all()
      return render(request, 'boarddocs/legaltop.html', {'p': n, })

@loginrequired
def historicaltop(request):
      n = Historical.objects.all()
      return render(request, 'boarddocs/historicaltop.html', {'p': n, })

@loginrequired
def gallery(request):
      n = Picture.objects.all()
      return render(request, 'boarddocs/gallery.html', {'p': n, })




