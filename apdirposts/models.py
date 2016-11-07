from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models.signals import post_save
from django.db.models.signals import pre_save

# python manage.py dumpdata <your_app> > temp_data.json
# python manage.py reset <your_app>
# python manage.py loaddata temp_data.json

class Director(models.Model):
   user = models.OneToOneField(User)
   def name(self):
      return self.user.get_full_name()
   title = models.CharField('Title: Ms., Mr., Dr., etc.', max_length=30, blank = True)
   nameinbyline = models.CharField('Name in bylines', max_length = 200, blank = True)
   formalname = models.CharField('Formal name', max_length = 200, blank = True)
   bio = models.TextField(blank = True)
   face = models.ImageField(upload_to = 'faces', blank = True, null = True)
   email = models.EmailField('Primary email', blank = True)
   phone = models.CharField('Primary phone', blank = True, max_length = 15)
   notes = models.TextField('Private notes', blank = True, null = True)
   def __unicode__(self):
      return self.name()

class Illustration(models.Model):
   pic = models.ImageField(upload_to = 'illustrations', blank = True, null = True)
   caption = models.TextField(blank = True)
   credit = models.TextField(blank = True)
   slideshow = models.BooleanField(default = False)
   target = models.URLField(blank = True, null = True)
   def __unicode__(self):
      n = self.pic
      return "%s: %s" % (n, self.caption[:70])

class Postcategory(models.Model):
   postcategory = models.CharField(max_length = 200)
   def __unicode__(self):
      return self.postcategory

class Post(models.Model):
   pub_date = models.DateTimeField('date published', blank = True, editable = False, null = True)
   title = models.CharField(max_length=200)
   author = models.ForeignKey(User)
   byline = models.CharField(max_length = 500, blank = True)
   publish = models.BooleanField()
   content = models.TextField(blank = True)
   illustrations = models.ManyToManyField(Illustration, null = True, blank = True)
   category = models.ForeignKey(Postcategory)
   promote = models.BooleanField(default = False)
   def __unicode__(self):
      return "%s, by %s" % (self.title, self.author)

class CommunityEvent(models.Model):
   author = models.ForeignKey(User)
   title = models.CharField(max_length=200)
   pub_date = models.DateTimeField('date published', blank = True, editable = False, null = True)
   on = models.DateTimeField('When')
   publish = models.BooleanField()
   content = models.TextField(blank = True)
   illustrations = models.ManyToManyField(Illustration, null = True, blank = True)
   def __unicode__(self):
     return self.title

class Event(models.Model):
   author = models.ForeignKey(User)
   title = models.CharField(max_length=200)
   pub_date = models.DateTimeField('date published', blank = True, editable = False, null = True)
   on = models.DateTimeField('When')
   end = models.DateTimeField('Until', null = True, blank = True)
   ebcode = models.CharField('EventBrite Code', max_length = 400, blank = True)
   rpost = models.ForeignKey(Post, related_name = "revent", null = True, blank = True)
   publish = models.BooleanField()
   content = models.TextField(blank = True)
   illustrations = models.ManyToManyField(Illustration, null = True, blank = True)
   free = models.BooleanField(default = False)
   def __unicode__(self):
       if self.end is not None:
           return "%s scheduled for %s until %s" % (self.title, self.on, self.end)
       else:
           return "%s scheduled for %s" % (self.title, self.on)

class Notice(models.Model):
   """For the "In the News" page."""
   on = models.DateTimeField('When', null = True)
   newslink = models.URLField(blank = True)
   pub_date = models.DateTimeField('date published', blank = True, editable = False, null = True)
   title = models.CharField(max_length=200)
   author = models.ForeignKey(User)
   content = models.TextField(blank = True)
   illustrations = models.ManyToManyField(Illustration, null = True, blank = True)
   
class Smile(models.Model):
  """Just to keep track of people clicking on the Amazon smile links."""
  click_date = models.DateTimeField('date clicked', blank = True, null = True)
  session_id = models.CharField(max_length=400, blank = True, null = True)

# register a handler for the signal django.db.models.signals.post_save on the User model, and, in the handler, if created=True, create the associated user profile.

def on_new_user(sender, created, instance, **kwargs):
   if created:
      nd = Director(user = instance)
      nd.save()

def on_save_user(sender, instance, **kwargs):
      try:
         nd = Director.objects.get(user = instance.id)
      except:
         pass
      else:
         saveit = False
         if not nd.nameinbyline: 
            nd.nameinbyline = instance.get_full_name()
            saveit = True
         if not nd.formalname:
            nd.formalname = nd.nameinbyline
            saveit = True
         if saveit: nd.save()

def on_dirpost_save(sender, instance, **kwargs):
   p = instance
   if p.publish and p.pub_date is None:
      p.pub_date = datetime.datetime.now()

post_save.connect(on_new_user, sender = User, dispatch_uid="nuser")
pre_save.connect(on_save_user, sender = User, dispatch_uid="cuser")
pre_save.connect(on_dirpost_save, sender = Post, dispatch_uid="dirpsave")
