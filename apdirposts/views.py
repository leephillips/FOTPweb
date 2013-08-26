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
                              'title': p.title})
