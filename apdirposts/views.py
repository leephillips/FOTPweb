from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from models import Director, Post, Illustration, Notice, Event
from datetime import datetime, timedelta

today = datetime.now()
RECENT = today - timedelta(days = 180)
SOON   = today + timedelta(days = 60)

def latest():
   #articles from the past RECENT days:
   articles = list(Post.objects.filter(pub_date__range = (RECENT, today)))
   #news mentions from the past RECENT days:
   notices = list(Notice.objects.filter(on__range = (RECENT, today)))
   #events coming up SOON:
   rawevents = Event.objects.filter(on__range = (today, SOON))
   #if they're not described in a related post:
   events = [e for e in rawevents if not e.rpost]
   #combine these into a list:
   return events + (articles + notices)[:7]   

def bio(request, who):
   n = Director.objects.get(user = int(who))
   return render_to_response('apdirposts/bio.html', {'w': n.formalname, 
                                                     'face': n.face.url })

def post(request, which):
   p = Post.objects.get(id = which)
   pics = Illustration.objects.filter(post=which)
   content = p.content
   return render(request, 'apdirposts/post.html',
                             {'illustrations': pics,
                              'content': content,
                              'latest': latest(),
                              'mainarticleone': 'thisone',
                              'byline': p.byline,
                              'title': p.title})

def posttop(request):
   return render(request, 'apdirposts/posttop.html', 
                 {'p': Post.objects.filter(category__postcategory = "front").order_by('-pub_date'),
                  'mainarticleone': 'thisone'
                 })

def front(request):
   return render(request, 'front.html')
