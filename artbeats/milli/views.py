from django.http import HttpResponse
from django.template import loader

from .entity.model import arts,artbeatproducts
def index(request):


  obj = arts.objects.first()
  products = artbeatproducts.objects.all()
  template = loader.get_template('index.html')
  context = {
    'title': 'Milli Artbeats Page','artist':getattr(obj,'title'),'teaser':getattr(obj,'descr'),'items':products
  }

  return HttpResponse(template.render(context,request))

def astedadari(request):
  my = loader.get_template('astedadari.html')
  context = {
    'title': 'Milli Artbeats Page', 'artist': 'Eyob'
  }
  return HttpResponse(my.render(context, request))