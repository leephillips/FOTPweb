from django.db import models
from django.contrib.auth.models import User
import datetime

class Director(models.Model):
   user = models.OneToOneField(User)
   def name(self):
      return self.get_full_name()
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
   
