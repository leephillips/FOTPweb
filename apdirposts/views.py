from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, get_object_or_404
from models import Director, Post, Illustration, Notice, Event
from datetime import datetime, timedelta

today = datetime.now()
RECENT = today - timedelta(days = 180)
SOON   = today + timedelta(days = 60)
# mm = Post.objects.get(id = 6)
# mm.pub_date = datetime.datetime(2013, 8, 1, 13, 13, 13)
# mm.save()
def latest(exclude = None):
   try:
      xid = int(exclude)
   except:
      xid = 0
    #articles from the past RECENT days (changed to SOON to deal with stale "today"):
   articles = list(Post.objects.filter(pub_date__range = (RECENT, SOON)).exclude(
                   category__postcategory = exclude).exclude(id = xid).exclude(
                   publish = False).order_by('-pub_date'))
   articles = zip(len(articles)*['post'],articles)[:9]
   #news mentions from the past RECENT days:
   notices = list(Notice.objects.filter(on__range = (RECENT, SOON)).exclude(id = xid).order_by('-pub_date'))
   notices = zip(len(notices)*['notice'],notices)[:9]
   #events coming up SOON:
   #if they're not described in a related post:
   if exclude == "events":
      events = []
   else:
      rawevents = Event.objects.filter(on__range = (today, SOON)).exclude(
                                       publish = False)
      events = [e for e in rawevents if not e.rpost]
      events = zip(len(events)*['event'],events)[:9]
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
   p = get_object_or_404(Post, id = which)
   r = Event.objects.filter(rpost = p).order_by('on')
   category = p.category.postcategory
   categoryclass = ['mainarticleone', 'cornerone', 'scienceone'][
                   ['main', 'corner', 'science'].index(category)]
   if p.publish:
      pics = Illustration.objects.filter(post=which)
      content = p.content
      if ("<iframe" in content or "<object" in content or
         "<embed" in content):
            template = "objpage.html"
      else:
            template = "post.html"
      return render(request, 'apdirposts/'+template,
                                {'illustrations': pics,
                                 'content': content,
                                 'author': p.author,
                                 'latest': latest(which),
                                 categoryclass: 'thisone',
                                 'byline': p.byline,
                                 'date' : p.pub_date,
                                 'events': r,
                                 'title': p.title})
   else:
      return HttpResponseRedirect("/")

def event(request, which):
   p = get_object_or_404(Event, id = which)
   p = Event.objects.get(id = which)
   if p.publish:
      pics = Illustration.objects.filter(event=which)
      doors = p.on - timedelta(minutes = 15)
      return render(request, 'apdirposts/event.html',
                                {'illustrations': pics,
                                 'content': p.content,
                                 'latest': latest(which),
                                 'eventone': 'thisone',
                                 'on': p.on,
                                 'doors': doors,
                                 'ebcode': p.ebcode,
                                 'rpost': p.rpost,
                                 'title': p.title})
   else:
      return HttpResponseRedirect("/")
                 
def notice(request, which):
   p = get_object_or_404(Notice, id = which)
   pics = Illustration.objects.filter(notice=which)
   return render(request, 'apdirposts/notice.html',
                             {'illustrations': pics,
                              'content': p.content,
                              'on': p.on,
                              'latest': latest(which),
                              'inthenewsone': 'thisone',
                              'newslink': p.newslink,
                              'title': p.title})
   
def join(request):
   return render(request, 'apdirposts/join.html',
                 {'joinone': 'thisone',
                  'latest': latest()}
                )

def about(request):
   return render(request, 'apdirposts/about.html',
                 {'aboutone': 'thisone',
                  'latest': latest()}
                )

def starchart(request):
   return render(request, 'apdirposts/apppage.html',
                 {'framed': 'http://lee-phillips.org/arlplanet/skymaps/skymap.html',
                  'title': 'The sky above Arlington, Virginia',
                  'intro': 'The map is initially displayed at the current time. Choose other times using the column at the right, and change the overlayed information using the buttons at the bottom.&nbsp; Star charts generated by <a href="http://stellarium.org">Stellarium</a>.',
                  'afternotes': 'The overlays use transparent PNGs, which do not work on older versions of Internet Explorer. Please direct comments or questions to <a href="mailto:lee@lee-phillips.org">Lee Phillips</a>.'
                 })

def movies(request):
   return render(request, 'apdirposts/movies.html',
                 {'aboutone': 'thisone',
                  'latest': latest()}
                )

def donate(request):
   return render(request, 'apdirposts/donate.html',
                 {'joinone': 'thisone',
                  'latest': latest()}
                )

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
