from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.shortcuts import render, redirect
from django.template import loader
from .entity.model import arts,artsadmin
from django.contrib.auth.decorators import login_required


@login_required(login_url='/userlogin')
def index(request):


   title =''
   descr = ''

   obj = arts.objects.first()
   title = getattr(obj,'title')
   descr = getattr(obj,'descr')
   my = loader.get_template('alekaform.html')


   context = {
    'title': 'Milli Artbeats Page', 'artist': 'Admins','title':title,'descr':descr
    }

   t = loader.get_template("form.html")
   return HttpResponse(my.render(context, request))

def userlogin(request):


  message = ""
  my = loader.get_template('astedadari.html')

  if request.method == 'POST':
    username = request.POST.get('login','ts')
    password = request.POST.get('password','tp')
    user = authenticate(username=username, password=password)
    if user is not None:
     login(request,user)
     message = "Good TO GO"
    else:
     message = "Problem"


    return redirect ("/aleka?"+message)

  else:
      context = {
          'title': 'Milli Artbeats Page', 'artist': message
      }
      return HttpResponse(my.render(context, request))

      #(my.render(context, request))
def userlogout(request):
    logout(request)
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