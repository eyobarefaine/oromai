from django.http import HttpResponse
from django.template import loader

from .arts import Arts
def index(request):

  arts = Arts(1)
  a = arts.getArtName()
  print (a)

  template = loader.get_template('index.html')
  context = {
    'title': 'Milli Artbeats Page'
  }
  return HttpResponse(template.render(context,request))