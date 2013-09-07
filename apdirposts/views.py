from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from models import Director, Post, Illustration, Notice, Event
from datetime import datetime, timedelta

today = datetime.now()
RECENT = today - timedelta(days = 180)
SOON   = today + timedelta(days = 60)

def latest(exclude = None):
   try:
      xid = int(exclude)
   except:
      xid = 0
    #articles from the past RECENT days:
   articles = list(Post.objects.filter(pub_date__range = (RECENT, today)).exclude(
                   category__postcategory = exclude).exclude(id = xid).exclude(
                   publish = False))
   articles = zip(len(articles)*['post'],articles)[:4]
   #news mentions from the past RECENT days:
   notices = list(Notice.objects.filter(on__range = (RECENT, today)))
   notices = zip(len(notices)*['notice'],notices)[:4]
   #events coming up SOON:
   #if they're not described in a related post:
   if exclude == "events":
      events = []
   else:
      rawevents = Event.objects.filter(on__range = (today, SOON)).exclude(
                                       publish = False)
      events = [e for e in rawevents if not e.rpost]
      events = zip(len(events)*['event'],events)[:4]
   if exclude == "notices":
      notices = []
   #combine these into a list:
   return events + articles + notices

def bio(request, who):
   n = Director.objects.get(user = int(who))
   try:
      face = n.face.url
   except:
      face = ""
   return render(request, 'apdirposts/bio.html', 
                             {'w': n.formalname, 
                              'face': face,
                              'bio': n.bio,
                             })

def post(request, which):
   p = Post.objects.get(id = which)
   categoryclass = ['mainarticleone', 'cornerone', 'scienceone'][
                   ['main', 'corner', 'science'].index('science')]
   if p.publish:
      pics = Illustration.objects.filter(post=which)
      content = p.content
      return render(request, 'apdirposts/post.html',
                                {'illustrations': pics,
                                 'content': content,
                                 'author': p.author,
                                 'latest': latest(which),
                                 categoryclass: 'thisone',
                                 'byline': p.byline,
                                 'title': p.title})
   else:
      return HttpResponseRedirect("/")

def event(request, which):
   p = Event.objects.get(id = which)
   if p.publish:
      pics = Illustration.objects.filter(notice=which)
      return render(request, 'apdirposts/event.html',
                                {'illustrations': pics,
                                 'content': p.content,
                                 'latest': latest(which),
                                 'eventone': 'thisone',
                                 'on': p.on,
                                 'ebcode': p.ebcode,
                                 'title': p.title})
   else:
      return HttpResponseRedirect("/")
                 
def notice(request, which):
   p = Notice.objects.get(id = which)
   if p.publish:
      pics = Illustration.objects.filter(notice=which)
      return render(request, 'apdirposts/notice.html',
                                {'illustrations': pics,
                                 'content': p.content,
                                 'latest': latest(which),
                                 'inthenewsone': 'thisone',
                                 'newslink': p.newslink,
                                 'title': p.title})
   else:
      return HttpResponseRedirect("/")
   
def eventtop(request):
   return render(request, 'apdirposts/eventtop.html', 
                 {'p': Event.objects.filter(on__gte = today).order_by('on').exclude(
                  publish = False),
                  'latest': latest('events'),
                  'eventone': 'thisone',
                 })

def noticetop(request):
   return render(request, 'apdirposts/noticetop.html', 
                 {'p': Notice.objects.all().order_by('-pub_date'),
                  'inthenewsone': 'thisone',
                  'latest': latest('notice'),
                 })

def cornertop(request):
   return render(request, 'apdirposts/cornertop.html', 
                 {'p': Post.objects.filter(category__postcategory = "corner").order_by(
                  '-pub_date').exclude(publish = False),
                  'cornerone': 'thisone',
                  'latest': latest('corner'),
                 })

def sciencetop(request):
   return render(request, 'apdirposts/sciencetop.html', 
                 {'p': Post.objects.filter(category__postcategory = "science").order_by(
                  '-pub_date').exclude(publish = False),
                  'scienceone': 'thisone',
                  'latest': latest('science'),
                 })

def posttop(request):
   return render(request, 'apdirposts/posttop.html', 
                 {'p': Post.objects.filter(category__postcategory = "main").order_by(
                  '-pub_date').exclude(publish = False),
                  'mainarticleone': 'thisone',
                  'latest': latest('main'),
                 })

def front(request):
   return render(request, 'front.html',
                {'latest': latest()})
