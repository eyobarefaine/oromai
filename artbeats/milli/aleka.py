from django.http import HttpResponse
from django.template import loader
from .arts import Arts
def index(request):

  my = loader.get_template('astedadari.html')
  context = {
    'title': 'Milli Artbeats Page', 'artist': 'Admin Login'
  }
  return HttpResponse(my.render(context, request))

def login(request):
  arts = Arts("")

  my = loader.get_template('astedadari.html')

  if request.method == 'POST':
    login = request.POST.get('login','')
    password = request.POST.get('password','')
    check = arts.check(login,password)
    if (check):
      message = "Way to go"
    else:
      message = "no cando"

      context = {
        'title': 'Milli Artbeats Page', 'artist': message
      }

    return HttpResponse(my.render(context, request))