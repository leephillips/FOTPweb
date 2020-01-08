from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, render, get_object_or_404
from django.views.decorators.clickjacking import xframe_options_exempt
from models import *
from datetime import datetime, timedelta
import re
from django import forms
from django.forms.models import modelformset_factory
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from tinymce.widgets import TinyMCE
from django.conf  import settings
from decimal import *
import string
import random

chars = string.letters + string.digits
now = datetime.now # to be called in views to get the fresh now
today = datetime.now()
RECENT = today - timedelta(days = 180)
SOON   = today + timedelta(days = 60)
REALSOON  = today + timedelta(days = 4)
# mm = Post.objects.get(id = 6)
# mm.pub_date = datetime.datetime(2013, 8, 1, 13, 13, 13)
# mm.save()

def sql_cleanup(s):
    return s.replace("\r", " - ").replace("\m", " - ").replace("\n", " - ").replace("\j", " - ")

def ticketing(request, id):
    """The post id is main article describing weekend. Looks up all event objects linked
    to the post. For each object, uses Eventbrite API to create an event page on Eventbrite,
    and creates all the usual tickets. Returns event id and adds it to event object.
    Makes all the Eventbrite events live, and publishes the main post and all event posts,
    unless a delay is requested."""
    mainpost = Post.objects.get(id = id)
    events = Event.objects.filter(rpost = id)
    if request.method == 'POST': #We're going for it
        if request.POST.get('delay') == 'yes':
            delay = True
        else:
            delay = False
        from eventbrite import Eventbrite
        eventbrite = Eventbrite(settings.TOKEN)
        capacity = 38
        eventzone = "America/New_York"
        t1 = {'ticket_class.name': 'Children (under 12)', 'ticket_class.cost': 'USD,300', 'ticket_class.quantity_total': capacity} 
        t2 = {'ticket_class.name': 'Member', 'ticket_class.cost': 'USD,500', 'ticket_class.quantity_total': capacity} 
        t3 = {'ticket_class.name': 'Adult', 'ticket_class.cost': 'USD,500', 'ticket_class.quantity_total': capacity} 
        t4 = {'ticket_class.name': 'Senior (60+)', 'ticket_class.cost': 'USD,300', 'ticket_class.quantity_total': capacity} 
        t5 = {'ticket_class.name': 'Support new programs for the Planetarium!', 'ticket_class.donation': True} 
        t1free = {'ticket_class.name': 'Children (under 12)', 'ticket_class.free': True, 'ticket_class.quantity_total': capacity} 
        t2free = {'ticket_class.name': 'Member', 'ticket_class.free': True, 'ticket_class.quantity_total': capacity} 
        t3free = {'ticket_class.name': 'Adult', 'ticket_class.free': True, 'ticket_class.quantity_total': capacity} 
        t4free = {'ticket_class.name': 'Senior (60+)', 'ticket_class.free': True, 'ticket_class.quantity_total': capacity} 
        t5free = {'ticket_class.name': 'Support new programs for the Planetarium!', 'ticket_class.donation': True} 
        tickets = [t1, t2, t3, t4, t5]
        freetickets = [t1free, t2free, t3free, t4free, t5free]
        evresponse = {}
        tkresponse = []
        for e in events:
            if e.ebcode is None or len(e.ebcode) < 3:
                eventname = e.title
                pics = Illustration.objects.filter(event=e.id)
                if len(pics) > 0:
                   content = picparse(e.content, pics)
                else:
                   content = e.content
                eventdescription = content
                eventstart = loctime2ev(e.on)
                if e.end:
                    eventend = loctime2ev(e.end)
                else:
                    eventend = loctime2ev(e.on + timedelta(minutes = 60))
                #make a new event
                event = eventbrite.post_event({'event.name.html':eventname, 'event.description.html':eventdescription,
                                             'event.start.utc':eventstart, 'event.end.utc':eventend,
                                             'event.start.timezone':eventzone, 'event.end.timezone':eventzone,
                                             'event.currency': 'USD', 'event.capacity': capacity})
                evresponse['event'] = event
                #make tickets
                if e.free:
                    ticketlist = freetickets
                else:
                    ticketlist = tickets
                for ticket in ticketlist:
                    tkresponse.append(eventbrite.post_event_ticket_class(event.get('id'), ticket))
                evresponse['tickets'] = tkresponse
                e.ebcode = event.get('id') #For the ticketing box on our website
            if not delay and e.publish == False:
                e.publish = True
            e.save()
            #eventbrite.publish_event(event.get('id')) #make live on Eventbrite - does not work, API incomplete.
        if not delay and mainpost.publish == False:
            mainpost.publish = True
            mainpost.save()
    else: # Last chance to bail.
        pass        
    return render(request, 'ticketing.html', locals())

def loctime2ev(t):
    """converting times to UTC and formatting for Eventbrite"""
    import pytz
    eastern = pytz.timezone('US/Eastern')
    fmt = '%Y-%m-%dT%H:%M:%SZ'
    utc = pytz.utc
    locdt = eastern.localize(t) #t must be a datetime
    utcdt = locdt.astimezone(utc)
    return  utcdt.strftime(fmt)

@login_required
def publishweekend(request):
    now = datetime.now()
    wlst = [] #Will be list of weekends with future events
    for e in futureevents():
        if e.rpost not in wlst:
            wlst.append(e.rpost)
    wlst = [[w] for w in wlst]
    for w in wlst:
        w.append(list(Event.objects.filter(rpost = w[0].id)))
    # utctime = events[0].on
    return render(request, 'weekendsummary.html', locals())

def futureevents():
    now = datetime.now()
    then = datetime(2030, 1, 1)
    events = Event.objects.filter(on__range = (now, then)).exclude(publish = True)
    return events

class NewArticleForm(forms.Form):
  byline = forms.CharField(max_length = '500')
  author = forms.CharField(widget=forms.HiddenInput())
  title = forms.CharField(max_length = '300')
  content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
  publish = forms.BooleanField()

class EclipseForm(forms.Form):
    title = forms.CharField(max_length=50)
    photographer = forms.CharField(max_length = 100)
    email = forms.EmailField()
    notes = forms.CharField(max_length = 500, widget=forms.Textarea)
    image = forms.ImageField()

class DonationForm(forms.Form):
    PURPOSE = (
        ('New', 'New membership'),
        ('Renewing', 'Renewing membership'))
    MEMBER_TYPE = (
        ('Nomembership', 'I am not purchasing a membership.'),
        ('Individual', '$15 - Individual'),
        ('Family', '$25 - Family'),
        ('Sponsor', '$50 - Sponsor'),
        ('Patron', '$100 - Patron'),
        ('Lifetime', '$1,000 - Lifetime'))
    PHONE_TYPE = (
        ('Mobile', 'Mobile'),
        ('Home', 'Home'),
        ('Work', 'Work'))
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    middle_name = forms.CharField(max_length=100, required = False)
    suffix_name = forms.CharField(max_length=10, required = False)
    purpose = forms.ChoiceField(choices = PURPOSE, widget = forms.RadioSelect, required = False)
    member_type = forms.ChoiceField(choices = MEMBER_TYPE, widget = forms.RadioSelect, required = True, initial=False)
    mailing_street = forms.CharField(max_length=100, required = False)
    mailing_city = forms.CharField(max_length=100, required = False)
    mailing_state = forms.CharField(max_length=100, required = False)
    mailing_zip = forms.CharField(max_length=30, required = False)
    phone = forms.CharField(max_length=30, required = False)
    phone_type = forms.ChoiceField(choices = PHONE_TYPE)
    email = forms.EmailField()
    wants_email = forms.BooleanField(required=False, initial=True)
    comments = forms.CharField(max_length = 250, required = False, widget=forms.Textarea(attrs={'placeholder':'Any comments.'}))
    donation = forms.DecimalField(max_digits=8, decimal_places=2, required = False, min_value=Decimal('0.00'))
    brown_donation = forms.DecimalField(max_digits=8, decimal_places=2, required = False, min_value=Decimal('0.00'))
    def clean(self):
        c = super(DonationForm, self).clean()
        purpose = c.get('purpose')
        member_type = c.get('member_type')
        # If user purchases a donation we need to know if it is a new one or a renewal.
        if member_type != 'Nomembership':
            if purpose == '': #Did not indicate a purpose
                self.add_error('purpose', 'Please indicate if this is a new membership or a renewal.')




def donationpage(request):
   form = DonationForm()
   return render(request, 'donationpage.html', locals())

def givingtuesday(request):
   form = DonationForm()
   return render(request, 'givingTuesday2019.html', locals())

def donation_submit(request):
    """Gather information, store in Supporter table in DB, and direct to information check on the way to Paypal."""
    member_prices = {'Nomembership': 0., 'Individual': 15., 'Family': 25., 'Sponsor': 50., 'Patron': 100., 'Lifetime': 1000.}
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            c = form.cleaned_data
            #Calculate total
            try:
                membershipCharge = member_prices[c['member_type']] or 0.0
            except:
                membershipCharge = 0.0
            try:
                donationCharge = c['donation'] or 0.0
            except:
                donationCharge = 0.0
            try:
                brownCharge = c['brown_donation'] or 0.0
            except:
                brownCharge = 0.0
            #generate invoice string
            orders = 1
            while orders:  # Check that we haven't used this invoice string already
              invoice = "".join(random.sample(chars, 5))
              orders = Supporter.objects.filter(invoice = invoice)
            c['invoice'] = invoice
            c['comments'] = sql_cleanup(c['comments'])
            new_supporter = Supporter(**c)
            new_supporter.total = Decimal(membershipCharge) + Decimal(donationCharge) + Decimal(brownCharge)
            new_supporter.save()
            c['donation'] = float(c['donation'] or '0.00') #Can't send Decimals through the session
            c['brown_donation'] = float(c['brown_donation'] or '0.00') #Can't send Decimals through the session
            c['membershipCharge'] = membershipCharge
            c['total'] = float(new_supporter.total)            
            request.session['c'] = c
            return HttpResponseRedirect('/donation_topaypal/')
        else:
            errormessage = "Please correct the errors below."
            return render(request, 'donationpage.html', {'form': form, 'errormessage': errormessage})
    else:
        return HttpResponseRedirect('/donationpage/')

def tuesday_submit(request):
    """Gather information, store in Supporter table in DB, and direct to information check on the way to Paypal."""
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            c = form.cleaned_data
            try:
                brownCharge = c['brown_donation'] or 0.0
            except:
                brownCharge = 0.0
            #generate invoice string
            orders = 1
            while orders:  # Check that we haven't used this invoice string already
              invoice = "".join(random.sample(chars, 5))
              orders = Supporter.objects.filter(invoice = invoice)
            c['invoice'] = invoice
            new_supporter = Supporter(**c)
            # new_supporter.total = Decimal(brownCharge)
            new_supporter.total = Decimal(brownCharge)
            new_supporter.comments = new_supporter.comments + "***Giving Tuesday***"
            new_supporter.save()
            c['donation'] = float(c['donation'] or '0.00') #Can't send Decimals through the session
            c['brown_donation'] = float(c['brown_donation'] or '0.00') #Can't send Decimals through the session
            c['total'] = float(new_supporter.total)            
            request.session['c'] = c
            return HttpResponseRedirect('/tuesday_topaypal/')
        else:
            errormessage = "Please correct the errors below."
            return render(request, 'donationpage.html', {'form': form, 'errormessage': errormessage})
    else:
        return HttpResponseRedirect('/donationpage/')

def donation_topaypal(request):
    c = request.session.get('c')
    return render(request, 'donation_topaypal.html', {'c': c})

def tuesday_topaypal(request):
    c = request.session.get('c')
    return render(request, 'tuesday_topaypal.html', {'c': c})

def return_from_paypal(request):
  #Upon return from Paypal.
  #https://developer.paypal.com/docs/classic/ipn/integration-guide/IPNandPDTVariables/#id092BE0U605Z
  #Account settings apparently do not permit return values, so we'll just say thanks.
  return render(request, 'donation_thanks.html', locals())

def sup_to_csv(request, cachekill):
    sups = Supporter.objects.all().order_by('date')
    ssa = [', '.join(['date', 'first_name', 'last_name', 'middle_name', 'suffix_name',
                             'purpose', 'member_type', 'mailing_street', 'mailing_city', 'mailing_state',
                             'mailing_zip', 'phone', 'phone_type', 'email', 'wants_email',
                             'comments', 'donation', 'brown_donation', 'total'])]
    for sup in sups:
        ssa.append(', '.join([str(sup.date).replace(","," "), str(sup.first_name).replace(","," "), str(sup.last_name).replace(","," "), str(sup.middle_name).replace(","," "), str(sup.suffix_name).replace(","," "), 
                             str(sup.purpose).replace(","," "), str(sup.member_type).replace(","," "), str(sup.mailing_street).replace(","," "), str(sup.mailing_city).replace(","," "), str(sup.mailing_state).replace(","," "),
                             str(sup.mailing_zip).replace(","," "), str(sup.phone).replace(","," "), str(sup.phone_type).replace(","," "), str(sup.email).replace(","," "), str(sup.wants_email).replace(","," "),
                             str(sup.comments).replace(","," "), str(sup.donation).replace(","," "), str(sup.brown_donation), str(sup.total)]))
    return HttpResponse("\n".join(ssa))

@login_required
def newarticle(request, pid = None):
   main = Postcategory.objects.filter(postcategory = 'main')[0]
   user = request.user
   existingposts = Post.objects.all().order_by('-pub_date')
   illustrations = Illustration.objects.all()
   if request.method == 'POST': #Hit the Save button
     if request.POST.get('publish') == 'on':
       publish = True
     else:
       publish = False
     munged = request.POST.get('content')
     if pid == None: # New article
       newpost = Post(title = request.POST.get('title'), author = user, publish = publish,
                      content = munged, category = main,
                      byline = request.POST.get('byline'))
       newpost.save()
       pid = newpost.id
       # kill = 1./0
     else: # Editing existing article
       existingpost = Post.objects.get(id = pid)
       existingpost.content = munged
       existingpost.title = request.POST.get('title')
       existingpost.publish = publish
       existingpost.byline = request.POST.get('byline')
       existingpost.save()
     thepost = Post.objects.get(id = pid) #retrieve saved version for populating form
     form = NewArticleForm(initial = {'content': thepost.content,
                                      'byline': thepost.byline, 'title': thepost.title,
                                      'publish': thepost.publish})
   else: #Did not hit the Save button
     if pid:
       newone = False
       existingpost = Post.objects.get(id = pid)
       form = NewArticleForm(initial = {'content': existingpost.content,
                                        'byline': existingpost.byline, 'title': existingpost.title,
                                        'publish': existingpost.publish})
     else:
       form = NewArticleForm(initial = {'author': user.id, 'byline': user.director.name})
       newone = True
   return render(request, 'newarticle.html', locals())

def thermo000888(request):
   today = now()
   latestentries = latest()
   smiled = request.session.get('smiled')
   rsevents = Event.objects.filter(on__range = (today, REALSOON)).exclude(
                                       publish = False).count()
   return render(request, 'front-thermo.html', locals())

def smile(request):
  now = datetime.now()
  smiled = request.session.get('smiled')
  if not smiled:
    request.session['smiled'] = str(now)
    Smile(click_date = now, session_id = str(now)).save() 
  return HttpResponseRedirect("http://smile.amazon.com/ch/27-2760025")

@login_required
def configure_slideshow(request):
   ilform = modelformset_factory(Illustration, extra = 0, fields = ['pic', 'slideshow'])
   if request.method == 'POST':
     ilformset = ilform(request.POST)
     if ilformset.is_valid():
       ilformset.save() 
     return HttpResponseRedirect("")
   else:
     ilformset = ilform(queryset = Illustration.objects.all().order_by('-slideshow'))
   return render(request, 'configure_slideshow.html', locals())
  
def preview_latest(exclude = None):
   today = now()
   try:
      xid = int(exclude)
   except:
      xid = 0
   #draft articles 
   articles = list(Post.objects.all().exclude(publish = True))
   for a in articles:
     if len(a.title) == 0:
       a.title = 'UNTITLED'
   articles = zip(len(articles)*['post'],articles)
   # articles = list(Post.objects.all().exclude(publish = True))
   #news mentions from the past RECENT days:
   # notices = list(Notice.objects.filter(on__range = (RECENT, SOON)).exclude(id = xid).order_by('-pub_date'))
   # notices = zip(len(notices)*['notice'],notices)[:9]
   # #events coming up SOON:
   # #if they're not described in a related post:
   # if exclude == "events":
   events = []
   # else:
   #    rawevents = Event.objects.filter(on__range = (today, SOON))
   #    events = [e for e in rawevents if not e.rpost]
   #    events = zip(len(events)*['event'],events)[:9]
   # if exclude == "notices":
   notices = []
   #combine these into a list:
   return (events + articles + notices)

def latest(exclude = None, number = 9):
   today = now()
   try:
      xid = int(exclude)
   except:
      xid = 0
    #articles from the past RECENT days (changed to SOON to deal with stale "today"):
   promoted = list(Post.objects.filter(promote = True).order_by('-pub_date'))
   promoted = zip(len(promoted)*['post'],promoted)[:number]
   articles = list(Post.objects.filter(pub_date__range = (RECENT, SOON)).exclude(
                   category__postcategory = exclude).exclude(id = xid).exclude(
                   publish = False).exclude(promote = True).order_by('-pub_date'))
   articles = zip(len(articles)*['post'],articles)[:number]
   #news mentions from the past RECENT days:
   notices = list(Notice.objects.filter(on__range = (RECENT, SOON)).exclude(id = xid).order_by('-pub_date'))
   notices = zip(len(notices)*['notice'],notices)[:number]
   #events coming up SOON:
   #if they're not described in a related post:
   if exclude == "events":
      events = []
   else:
      rawevents = Event.objects.filter(on__range = (today, SOON)).exclude(
                                       publish = False)
      events = [e for e in rawevents if not e.rpost]
      events = zip(len(events)*['event'],events)[:number]
   if exclude == "notices":
      notices = []
   #combine these into a list:
   return (promoted + events + articles + notices)[:number]

def bio(request, who):
   try:
       n = get_object_or_404(Director, user = int(who))
   except:
      raise Http404
   try:
      face = n.face.url
   except:
      face = ""
   return render(request, 'apdirposts/bio.html', 
                             {'w': n.formalname, 
                              'face': face,
                              'bio': n.bio,
                              'latest': latest()
                             })

def piccredit(caption, credit):
   if caption and len(caption) > 3:
      caption = caption.strip()
      if caption[-1] not in ".!?":
         caption = caption + "."
   if credit and len(credit) > 3:
      credit = credit.strip()
      if credit[-1] not in ".!?":
         credit = credit + "."
      credit = """<span class = "picturecredit"><span class = "creditcredit">
                Credit: </span>%s</span>""" % credit
   return caption + credit

def picparse(s, pics, useillustration = True):
   if useillustration:
       pkstart = 1
   else:
       pkstart = 2 #Do not display first illustration on article page, only on front page.
   picins = """<div class = "%s" style = 'width: %s;'>
   <img src = "https://friendsoftheplanetarium.org%s" alt = "" />
                                <p class = "caption">%s</p></div>"""
   p = {}
   captions = {}
   widths = {}
   for i in pics:
     p[i.pic.url] = i.pic.width > 300 and 'postillustration' or 'postfloatleftillustration'
     captions[i.pic.url] = piccredit(i.caption, i.credit)
     if i.pic.width <= 300:
        widths[i.pic.url] = str(i.pic.width) + "px"
     else:
        widths[i.pic.url] = "100%"
   if '<<' in  s and '>>' in s: # Author using our special picture insertion markup
      while s.find('<<') >= 0:
         picmatch = False
         o = s.find('<<') 
         c = s.find('>>') 
         if c > 0:
            a = s[o+2 : c]
            for pic in p.keys()[pkstart-1:]:
               if a in pic:
                  s = s.replace(s[o:c+2], picins % (p[pic], widths[pic], pic, captions[pic]))
                  picmatch = True
                  break
            if not picmatch:
               #Author must have made a mistake (misspelled key?).
               s = s.replace(s[o:c+2], '')
         else:
            # Missing an end tag
            return s
      return s
   else:
      pk = p.keys()[pkstart-1:]
      if len(pk) > 0:
          s = picins % (p[pk[0]], widths[pk[0]], pk[0], captions[pk[0]]) + s
      if len(pk) == 1:
         return s
      return s + "\n".join([picins % (p[pic], widths[pic], pic, captions[pic]) 
                            for pic in pk[pkstart:]])

@login_required
def preview_post(request, which):
   p = get_object_or_404(Post, id = which)
   r = Event.objects.filter(rpost = p).order_by('on')
   category = p.category.postcategory
   categoryclass = ['mainarticleone', 'cornerone', 'scienceone'][
                   ['main', 'corner', 'science'].index(category)]
   pics = Illustration.objects.filter(post=which)
   content = p.content
   if len(pics) > 0:
      content = picparse(content, pics)
   if ("<iframe" in content or "<object" in content or
      "<embed" in content):
         template = "objpage.html"
   else:
         template = "post.html"
   return render(request, 'apdirposts/'+template,
                            {'content': content,
                             'author': p.author,
                             'latest': latest(which),
                             categoryclass: 'thisone',
                             'byline': p.byline,
                             'date' : p.pub_date,
                             'events': r,
                             'title': p.title})

def x7298inside(request, which):
   try:
      p = get_object_or_404(Post, id = which)
   except:
      raise Http404
   r = Event.objects.filter(rpost = p).order_by('on')
   category = p.category.postcategory
   categoryclass = ['mainarticleone', 'cornerone', 'scienceone'][
                   ['main', 'corner', 'science'].index(category)]
   if p.publish:
      pics = Illustration.objects.filter(post=which)
      content = p.content
      if len(pics) > 0:
         content = picparse(content, pics)
      return render(request, '7298inside.html',
                                {'content': content,
                                 'author': p.author,
                                 'latest': latest(which),
                                 categoryclass: 'thisone',
                                 'byline': p.byline,
                                 'date' : p.pub_date,
                                 'events': None,
                                 'title': p.title})
   else:
      return HttpResponseRedirect("/")

def post(request, which):
   try:
      p = get_object_or_404(Post, id = which)
   except:
      raise Http404
   r = Event.objects.filter(rpost = p).order_by('on')
   category = p.category.postcategory
   categoryclass = ['mainarticleone', 'cornerone', 'scienceone'][
                   ['main', 'corner', 'science'].index(category)]
   if p.publish:
      pics = Illustration.objects.filter(post=which)
      content = p.content
      if len(pics) > 0:
         content = picparse(content, pics, p.useillustration)
      if ("<iframe" in content or "<object" in content or
         "<embed" in content):
            template = "objpage.html"
      else:
            template = "post.html"
      return render(request, 'apdirposts/'+template,
                                {'content': content,
                                 'author': p.author,
                                 'latest': latest(which),
                                 categoryclass: 'thisone',
                                 'byline': p.byline,
                                 'date' : p.pub_date,
                                 'events': r,
                                 'title': p.title})
   else:
      return HttpResponseRedirect("/")

def community_event(request, which):
   try:
      p = get_object_or_404(CommunityEvent, id = which)
   except:
      raise Http404
   p = CommunityEvent.objects.get(id = which)
   if p.publish:
      pics = Illustration.objects.filter(event=which)
      if len(pics) > 0:
         content = picparse(p.content, pics)
      else:
         content = p.content
      return render(request, 'apdirposts/community_event.html',
                                {'content': content,
                                 'on': p.on,
                                 'title': p.title})
   else:
      return HttpResponseRedirect("/")

def event(request, which):
   try:
      p = get_object_or_404(Event, id = which)
   except:
      raise Http404
   p = Event.objects.get(id = which)
   if p.publish:
      pics = Illustration.objects.filter(event=which)
      if len(pics) > 0:
         content = picparse(p.content, pics)
      else:
         content = p.content
      doors = p.on - timedelta(minutes = 30)
      return render(request, 'apdirposts/event.html',
                                {'content': content,
                                 'latest': latest(which),
                                 'eventone': 'thisone',
                                 'on': p.on,
                                 'free': p.free,
                                 'doors': doors,
                                 'ebcode': p.ebcode,
                                 'rpost': p.rpost,
                                 'title': p.title})
   else:
      return HttpResponseRedirect("/")
                 
def notice(request, which):
   try:
      p = get_object_or_404(Notice, id = which)
   except:
      raise Http404
   pics = Illustration.objects.filter(notice=which)
   if len(pics) > 0:
      content = picparse(p.content, pics)
   else:
      content = p.content
   return render(request, 'apdirposts/notice.html',
                             {'content': content,
                              'on': p.on,
                              'latest': latest(which),
                              'inthenewsone': 'thisone',
                              'newslink': p.newslink,
                              'title': p.title})
   
def website(request):
   return render(request, 'apdirposts/website.html',
                 {'aboutone': 'thisone',
                  'latest': latest()}
                )

def planets(request):
   return render(request, 'apdirposts/planets.html',
                 {'joinone': 'thisone',
                  'latest': latest(),
                  'smiled': request.session.get('smiled')
                 }
                )

def sf2016(request):
   return render(request, 'apdirposts/sf2016.html',
                 {'joinone': 'thisone',
                  'latest': latest(),
                  'smiled': request.session.get('smiled')
                 }
                )

def join(request):
   return render(request, 'apdirposts/join.html',
                 {'joinone': 'thisone',
                  'latest': latest(),
                  'smiled': request.session.get('smiled')
                 }
                )

def about(request):
   return render(request, 'apdirposts/about.html',
                 {'aboutone': 'thisone',
                  'latest': latest()}
                )

############### new special pages ###############

def visit(request):
   return render(request, 'apdirposts/visit.html')

def corporation(request):
   return render(request, 'apdirposts/corporation.html')

def projects(request):
   return render(request, 'apdirposts/projects.html')

################################################

def starchart(request):
   return render(request, 'apdirposts/apppage.html',
                 {'framed': 'https://lee-phillips.org/arlplanet/skymaps/skymap.html',
                  'title': 'The sky above Arlington, Virginia',
                  'intro': 'The map is initially displayed at the current time. Choose other times using the column at the right, and change the overlayed information using the buttons at the bottom.&nbsp; Star charts generated by <a href="http://stellarium.org">Stellarium</a>.',
                  'afternotes': 'The overlays use transparent PNGs, which do not work on older versions of Internet Explorer.</a>.'
                 })

def movies(request):
   return render(request, 'apdirposts/movies.html',
                 {'moviesone': 'thisone',
                  'latest': latest()}
                )

def scholarship(request):
   return render(request, 'apdirposts/scholarship.html',
                 {'joinone': 'thisone',
                  'latest': latest()}
                )

def donate(request):
   return render(request, 'apdirposts/donate.html',
                 {'joinone': 'thisone',
                  'latest': latest()}
                )

def eventtop(request):
   today = now()
   return render(request, 'apdirposts/eventtop.html', 
                 {'p': Event.objects.filter(on__gte = today).order_by('on').exclude(
                  publish = False),
                  'latest': latest('events'),
                  'eventone': 'thisone',
                  'community_events': CommunityEvent.objects.filter(
                             on__gte = today).order_by('on').exclude(publish = False),

                 })

def noticetop(request):
   return render(request, 'apdirposts/noticetop.html', 
                 {'p': Notice.objects.all().order_by('-on'),
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
                 {'p': Post.objects.order_by(
                  '-pub_date').exclude(publish = False),
                  'mainarticleone': 'thisone',
                  'latest': '' ,
                 })

@login_required
def preview_front(request):
   today = now()
   latestentries = preview_latest()
   slides = Illustration.objects.filter(slideshow = True)
   smiled = request.session.get('smiled')
   rsevents = Event.objects.filter(on__range = (today, REALSOON)).count()
   return render(request, 'preview_front.html', locals())

def front(request):
   today = now()
   latestentries = latest()
   slides = Illustration.objects.filter(slideshow = True)
   promoted = Post.objects.filter(promote = True)   
   smiled = request.session.get('smiled')
   rsevents = Event.objects.filter(on__range = (today, REALSOON)).exclude(
                                       publish = False).count()
   return render(request, 'front.html', locals())

def x7297(request):
   today = now()
   latestentries = latest(number = 5)
   promoted = Post.objects.filter(promote = True)   
   slides = Illustration.objects.filter(slideshow = True)
   smiled = request.session.get('smiled')
   rsevents = Event.objects.filter(on__range = (today, REALSOON)).exclude(
                                       publish = False).count()
   return render(request, 'preview_slideshow.html', locals())

def x7298(request):
   today = now()
   latestentries = latest(number = 5)
   slides = Illustration.objects.filter(slideshow = True)
   return render(request, '7298.html', locals())


def x7297inside(request):
    return postx(request, 90)

@xframe_options_exempt
def aps_banner(request):
   today = now()
   rsevents = Event.objects.filter(on__range = (today, REALSOON)).exclude(
                                       publish = False)
   return render(request, 'aps_banner.html', locals())

def eclipse_upload(request):
    thanks = False
    if request.method == 'POST':
        form = EclipseForm(request.POST, request.FILES)
        if form.is_valid():
            eclipse = EclipseUpload(title = request.POST.get('title'),
                                    photographer = request.POST.get('photographer'),
                                    email = request.POST.get('email'),
                                    notes = request.POST.get('notes'),
                                    image = request.FILES.get('image')
                                   )
            eclipse.save()
            thanks = True
            return render(request, 'apdirposts/eclipse.html', locals())
    else:
        form = EclipseForm()
    return render(request, 'apdirposts/eclipse.html', locals())

@login_required
def eclipse_table(request):
    lines = EclipseUpload.objects.all().order_by('-uploaded_at')
    return render(request, 'boarddocs/eclipse_table.html', locals())
