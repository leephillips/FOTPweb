from django.shortcuts import render_to_response
from django.template import RequestContext

# This is in shortcuts.render:
# def show(template, data):
#    return render_to_response(template, data,
#                              context_instance=RequestContext(request),
#                               )
