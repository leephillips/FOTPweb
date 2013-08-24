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
   title = models.CharField( 'Title: Ms., Mr., Dr., etc.', max_length=30)
   nameinbyline = models.CharField('Name in bylines', max_length = 200)
   formalname = models.CharField('Formal name', max_length = 200)
   bio = models.TextField()
   # more fields: bio, contact
   def __unicode__(self):
      return self.name()

class Post(models.Model):
   pub_date = models.DateTimeField('date published', blank = True, editable = False, null = True)
   title = models.CharField(max_length=200)
   author = models.ForeignKey(User)
   byline = models.CharField(max_length = 500)
   publish = models.BooleanField()
   content = models.TextField(blank = True)
   # def save(self, *args, **kwargs):
   #    self.pub_date =  datetime.datetime.today()
   #    super(Post, self).save(*args, **kwargs)
   def __unicode__(self):
      return "%s, by %s" % (self.title, self.author)

# register a handler for the signal django.db.models.signals.post_save on the User model, and, in the handler, if created=True, create the associated user profile.

def on_new_user(sender, created, instance, **kwargs):
   if created == True:
      nd = Director(user = instance)
      nd.nameinbyline = instance.get_full_name()
      nd.formalname = instance.get_full_name()
      nd.save()

post_save.connect(on_new_user, sender = User, dispatch_uid="nuser")

def on_dirpost_save(sender, instance, **kwargs):
   p = instance
   if p.publish and p.pub_date is None:
      p.pub_date = datetime.datetime.now()

pre_save.connect(on_dirpost_save, sender = Post, dispatch_uid="dirpsave")
