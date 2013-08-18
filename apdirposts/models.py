from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models.signals import post_save

# python manage.py dumpdata <your_app> > temp_data.json
# python manage.py reset <your_app>
# python manage.py loaddata temp_data.json


class Director(models.Model):
   user = models.OneToOneField(User)
   def name(self):
      return self.user.get_full_name()
   title = models.CharField(max_length=30)
   nameinbyline = models.CharField(max_length = 200)
   formalname = models.CharField(max_length = 200)
   def __unicode__(self):
      return self.name()

class Post(models.Model):
   pub_date = models.DateTimeField('date published')
   title = models.CharField(max_length=200)
   author = models.ForeignKey(User)
   byline = models.CharField(max_length = 500)
   publish = models.BooleanField()
   content = models.TextField()
   def save(self, *args, **kwargs):
      self.pub_date =  datetime.datetime.today()
      super(Post, self).save(*args, **kwargs)
   def __unicode__(self):
      return "%s, by %s" % (self.title, self.author)

# register a handler for the signal django.db.models.signals.post_save on the User model, and, in the handler, if created=True, create the associated user profile.

def on_new_user(sender, created, instance, **kwargs):
   if created == True:
      # Director.objects.create(user = instance)      
      Director(user = instance).save()

post_save.connect(on_new_user, sender = User, dispatch_uid="nuser")
