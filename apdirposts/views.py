from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Director
def bio(request, who):
   n = Director.objects.get(user = int(who))
   return render_to_response('apdirposts/bio.html', {'w': n.formalname, 
                                                     'face': n.face.url })

