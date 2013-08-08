from django.db import models
from django.contrib.auth.models import User

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
   content = models.TextField()

