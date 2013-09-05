from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from models import Director, Post, Illustration

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
                              'mainarticleone': 'thisone',
                              'byline': p.byline,
                              'title': p.title})

def posttop(request):
   return render(request, 'apdirposts/posttop.html', 
                 {'p': Post.objects.all().order_by('-pub_date'),
                  'mainarticleone': 'thisone'
                 })

def front(request):
   return render(request, 'front.html')
