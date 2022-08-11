from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.shortcuts import render, redirect
from .entity.model import arts
from .entity.model import artsproducts,artscategory

@login_required(login_url='/userlogin')
def index(request):

        rows = artsproducts.objects.all().values()
        my = loader.get_template('alekaproducts.html')
        context = {
            'title': 'Milli Artbeats Page', 'artist': 'Admins', 'items': rows
        }
        return HttpResponse(my.render(context, request))
@login_required(login_url='/userlogin')
def add(request):

        category = artscategory.objects.all().values();
        my = loader.get_template('alekaaddproducts.html')
        context = {
            'title': 'Milli Artbeats Page', 'artist': 'Admins', 'item': category,'add':True
        }
        return HttpResponse(my.render(context, request))
@login_required(login_url='/userlogin')
def save(request):
        if request.method == 'POST':
                artsname_ = request.POST.get('artsname','')
                artsdescr_ = request.POST.get('artsdesc','')
                artsprice_ = request.POST.get('artsprice','')
                artscategory_= request.POST.get('artscategory','')
                artsproducts.objects.create(artsname=artsname_, artsdescr=artsdescr_,artsprice=artsprice_,artscatagory=artscategory_)
        return redirect("/aleka/products")

login_required(login_url='/userlogin')
def updaterecord(request):
        if request.method == 'POST':
                id_ = request.POST.get('id')
                obj = artsproducts.objects.get(id=id_)
                obj.artsname = request.POST.get('artsname','')
                obj.artsdescr = request.POST.get('artsdesc','')
                obj.artsprice = request.POST.get('artsprice','')
                obj.artscategory= request.POST.get('artscategory','')
                obj.save()
               # artsproducts.objects.create(artsname=artsname_, artsdescr=artsdescr_,artsprice=artsprice_,artscatagory=artscategory_)
        return redirect("/aleka/products")

@login_required(login_url='/userlogin')
def remove (request):
        if request.method == 'POST':
                id_ = request.POST.get('id','')
                artsproducts.objects.filter(id=id_).delete()
                return redirect("/aleka/products")

@login_required(login_url='/userlogin')
def edit(request):
       if request.GET.get('id'):
          id_ = request.GET.get('id')
          row = artsproducts.objects.filter(id=id_).values()
          category = artscategory.objects.all().values();
          my = loader.get_template('alekaaddproducts.html')
          context = {
                  'title': 'Milli Artbeats Page', 'artist': 'Admins', 'item': row,'edit':True, 'cats':category
          }
       return HttpResponse(my.render(context, request))


