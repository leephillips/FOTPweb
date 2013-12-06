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
   thefile = models.FileField(upload_to = "boarddocs/other")
   name = models.CharField('', max_length = 400, blank = True)
   def __unicode__(self):
      return self.name

class Annualreport(models.Model):
   user = models.ForeignKey(User)
   docname = "AnnualReport"
   whenUploaded = models.DateTimeField('whenUploaded') # Filled in with signal
   thefile = models.FileField(upload_to = "boarddocs/annualreports")
   name = models.CharField('', max_length = 400, blank = True) # Filled in with signal
   startDate = models.DateField('Start Date')
   endDate = models.DateField('End Date')
   def __unicode__(self):
      return self.name

class Budgetreport(models.Model):
   user = models.ForeignKey(User)
   docname = "Budgetreport"
   whenUploaded = models.DateTimeField('whenUploaded') # Filled in with signal
   thefile = models.FileField(upload_to = "boarddocs/budgetreports")
   name = models.CharField('', max_length = 400, blank = True) # Filled in with signal
   startDate = models.DateField('Start Date')
   endDate = models.DateField('End Date')
   def __unicode__(self):
      return self.name

class Minutes(models.Model):
   user = models.ForeignKey(User)
   docname = "MeetingMinutes"
   whenUploaded = models.DateTimeField('whenUploaded') # Filled in with signal
   thefile = models.FileField(upload_to = "boarddocs/minutes")
   name = models.CharField('', max_length = 400, blank = True) # Filled in with signal
   meetingDate = models.DateTimeField('Meeting Date')
   def __unicode__(self):
      return self.name

class Agenda(models.Model):
   user = models.ForeignKey(User)
   docname = "MeetingAgenda"
   whenUploaded = models.DateTimeField('whenUploaded') # Filled in with signal
   thefile = models.FileField(upload_to = "boarddocs/meetingAgendas")
   name = models.CharField('', max_length = 400, blank = True) # Filled in with signal
   meetingDate = models.DateTimeField('Meeting Date')
   def __unicode__(self):
      return self.name

class LegalDoc(models.Model):
   user = models.ForeignKey(User)
   whenUploaded = models.DateTimeField('whenUploaded') # Filled in with signal
   thefile = models.FileField(upload_to = "boarddocs/legaldocs")
   name = models.CharField('', max_length = 400, blank = True)
   def __unicode__(self):
      return self.name

class Historical(models.Model):
   user = models.ForeignKey(User)
   whenUploaded = models.DateTimeField('whenUploaded') # Filled in with signal
   thefile = models.FileField(upload_to = "boarddocs/historical")
   name = models.CharField('', max_length = 400, blank = True)
   def __unicode__(self):
      return self.name

class Picture(models.Model):
   pic = models.ImageField(upload_to = 'boarddocs/assortedPictures', blank = True, null = True)
   caption = models.TextField(blank = True)
   credit = models.TextField(blank = True)
   def __unicode__(self):
      n = self.pic
      return "%s: %s" % (n, self.caption[:70])

def on_annualreport_save(sender, instance, **kwargs):
   p = instance
   p.whenUploaded = datetime.datetime.now()
   p.name = p.docname + p.whenUploaded.isoformat()

def on_otherdoc_save(sender, instance, **kwargs):
   p = instance
   p.whenUploaded = datetime.datetime.now()

pre_save.connect(on_annualreport_save, sender = Annualreport, dispatch_uid="apfilesave")
pre_save.connect(on_annualreport_save, sender = Minutes, dispatch_uid="minutessave")
pre_save.connect(on_annualreport_save, sender = Agenda, dispatch_uid="agendasave")
pre_save.connect(on_annualreport_save, sender = Budgetreport, dispatch_uid="budgetsave")
pre_save.connect(on_otherdoc_save, sender = Historical, dispatch_uid="histosave")
pre_save.connect(on_otherdoc_save, sender = LegalDoc, dispatch_uid="legalsave")
pre_save.connect(on_otherdoc_save, sender = Boardfile, dispatch_uid="othersace")

