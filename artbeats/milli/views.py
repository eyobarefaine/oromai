from django.http import HttpResponse
from django.template import loader

from .arts import Arts
def index(request):

  arts = Arts(2)


  template = loader.get_template('index.html')
  context = {
    'title': 'Milli Artbeats Page','artist':arts.getTitle(),'teaser':arts.getTeaser()
  }
  return HttpResponse(template.render(context,request))

def astedadari(request):
  template = loader.get_template('index.html')
  context = {
    'title': 'Milli Artbeats Page', 'artist': ''
  }
  return HttpResponse(template.render(context, request))