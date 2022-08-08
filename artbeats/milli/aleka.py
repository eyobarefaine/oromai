from django.http import HttpResponse
from django.template import loader

from .arts import Arts
def index(request):

  my = loader.get_template('gallery.html')
  context = {
    'title': 'Milli Artbeats Page', 'artist': 'Eyob'
  }
  return HttpResponse(my.render(context, request))