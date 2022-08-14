from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.shortcuts import render, redirect
from .ArtbeatsProductForm import ProductForm
from .entity.model import arts
from .entity.model import artbeatproducts,artscategory

@login_required(login_url='/userlogin')
def index(request):

        rows = artbeatproducts.objects.all().values()
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
            'title': 'Milli Artbeats Page', 'artist': 'Admins', 'item': category,'add':True,
        }
        return HttpResponse(my.render(context, request))
@login_required(login_url='/userlogin')
def save(request):
        #if request.method == 'POST':
         ####    artscategory_= request.POST.get('artscategory','')
             #   artbeatproducts.objects.create(artsname=artsname_, artsdescr=artsdescr_,artsprice=artsprice_,artscatagory=artscategory_)
        form = ProductForm(request.POST, request.FILES)
        t="false"
        if form.is_valid():
            t="true"
            form.save()
        return redirect("/aleka/products?id="+t)

login_required(login_url='/userlogin')
def updaterecord(request):
        if request.method == 'POST':
                id_ = request.POST.get('id')
                obj = artbeatproducts.objects.get(id=id_)
                obj.artsname = request.POST.get('artsname','')
                obj.artsdescr = request.POST.get('artsdesc','')
                obj.artsprice = request.POST.get('artsprice','')
                obj.artscategory= request.POST.get('artscategory','')
                artbeatproducts.save(obj)
               # artsproducts.objects.create(artsname=artsname_, artsdescr=artsdescr_,artsprice=artsprice_,artscatagory=artscategory_)
        return redirect("/aleka/products")

@login_required(login_url='/userlogin')
def remove (request):
        if request.method == 'POST':
                id_ = request.POST.get('id','')
                artbeatproducts.objects.filter(id=id_).delete()
                return redirect("/aleka/products")

@login_required(login_url='/userlogin')
def edit(request):
       if request.GET.get('id'):
          id_ = request.GET.get('id')
          row = artbeatproducts.objects.filter(id=id_).values()
          category = artscategory.objects.all().values();
          my = loader.get_template('alekaaddproducts.html')
          context = {
                  'title': 'Milli Artbeats Page', 'artist': 'Admins', 'item': row,'edit':True, 'cats':category
          }
       return HttpResponse(my.render(context, request))


