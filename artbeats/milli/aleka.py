from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .entity.model import arts,artsadmin


def index(request):


  title =''
  descr = ''

  if request.session.get("aleka"):

   obj = arts.objects.first()
   title = getattr(obj,'title')
   descr = getattr(obj,'descr')
   my = loader.get_template('alekaform.html')

  else:
    my = loader.get_template('astedadari.html')
  context = {
    'title': 'Milli Artbeats Page', 'artist': 'Admins','title':title,'descr':descr
  }
  return HttpResponse(my.render(context, request))

def login(request):



  my = loader.get_template('astedadari.html')

  if request.method == 'POST':
    login = request.POST.get('login','ts')
    password = request.POST.get('password','tp')

    field_user = 'usersname'
    field_pass = 'password'
    obj = artsadmin.objects.first()
    username = getattr(obj, field_user)
    password_ = getattr(obj,field_pass)
    if (username==login and password == password_):
      message = " Hello "+ login
      request.session["aleka"]=login
      return redirect ("/aleka")
    else:
      message = "No cando"

    context = {
        'title': 'Milli Artbeats Page', 'artist': message
    }


    return HttpResponse(my.render(context, request))
def logout(request):
    del request.session["aleka"]
    return redirect("/")

def save(request):
    if not request.session.get("aleka"):
        return redirect("/aleka?session=null")
    if request.method == 'POST':
        title_ = request.POST.get("title",'')
        descr_ = request.POST.get("descr",'')

        obj = arts.objects.first()


        obj.title = title_
        obj.descr = descr_
        obj.save()


    return redirect("/aleka")