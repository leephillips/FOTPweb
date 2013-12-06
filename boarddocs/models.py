from django.db import models
from django.contrib.auth.models import User
from ap import settings
import datetime
from django.db.models.signals import post_save
from django.db.models.signals import pre_save


class Boardfile(models.Model):
   user = models.ForeignKey(User)
   docname = "generic"
   whenUploaded = models.DateTimeField('whenUploaded') # Filled in with signal
   thefile = models.FileField(upload_to = "other")
   name = models.CharField('', max_length = 400, blank = True) # Filled in with signal
   covering = models.DateTimeField('Covering')
   def __unicode__(self):
      return self.name

class Annualreport(models.Model):
   user = models.ForeignKey(User)
   docname = "AnnualReport"
   whenUploaded = models.DateTimeField('whenUploaded') # Filled in with signal
   thefile = models.FileField(upload_to = "annualreports")
   name = models.CharField('', max_length = 400, blank = True) # Filled in with signal
   startDate = models.DateField('Start Date')
   endDate = models.DateField('End Date')
   def __unicode__(self):
      return self.name

class Minutes(models.Model):
   user = models.ForeignKey(User)
   docname = "MeetingMinutes"
   whenUploaded = models.DateTimeField('whenUploaded') # Filled in with signal
   thefile = models.FileField(upload_to = "minutes")
   name = models.CharField('', max_length = 400, blank = True) # Filled in with signal
   meetingDate = models.DateTimeField('Meeting Date')
   def __unicode__(self):
      return self.name

class Agenda(models.Model):
   user = models.ForeignKey(User)
   docname = "MeetingAgenda"
   whenUploaded = models.DateTimeField('whenUploaded') # Filled in with signal
   thefile = models.FileField(upload_to = "meetingAgendas")
   name = models.CharField('', max_length = 400, blank = True) # Filled in with signal
   meetingDate = models.DateTimeField('Meeting Date')
   def __unicode__(self):
      return self.name

def on_annualreport_save(sender, instance, **kwargs):
   p = instance
   p.whenUploaded = datetime.datetime.now()
   p.name = p.docname + p.whenUploaded.isoformat()

pre_save.connect(on_annualreport_save, sender = Annualreport, dispatch_uid="apfilesave")
pre_save.connect(on_annualreport_save, sender = Minutes, dispatch_uid="minutessave")
pre_save.connect(on_annualreport_save, sender = Agenda, dispatch_uid="agendasave")

