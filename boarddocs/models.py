from django.db import models
from django.contrib.auth.models import User
from ap import settings
import datetime
from django.db.models.signals import post_save
from django.db.models.signals import pre_save


def getDocName(f, s):
   return settings.MEDIA_ROOT+f.docdir+f.docnam+datetime.datetime.now().isoformat()


class Boardfile(models.Model):
   user = models.ForeignKey(User)
   docdir = "other/" # must have the trailing slash
   docname = "generic"
   whenUploaded = models.DateTimeField('whenUploaded') # Filled in with signal
   upload_to = settings.MEDIA_ROOT + docdir + docname + "%F-%T" 
   name = models.CharField('', max_length = 400, blank = True) # Filled in with signal
   covering = models.DateTimeField('Covering')
   def __unicode__(self):
      return self.name

class Annualreport(Boardfile):
   docdir = "annualreports/"
   docname = "AnnualReport"

class Minutes(Boardfile):
   docdir = "minutes/"
   docname = "MeetingMinutes"

def on_boardfile_save(sender, instance, **kwargs):
   p = instance
   p.whenUploaded = datetime.datetime.now()
   p.name = p.docname + p.whenUploaded.isoformat()

pre_save.connect(on_boardfile_save, sender = Boardfile, dispatch_uid="boardfilesave")

