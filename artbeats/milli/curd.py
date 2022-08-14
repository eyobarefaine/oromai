from .entity.model import arts
from .entity.model import artsadmin,artscategory
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def populate(self):
 # arts.objects.create(title="Million Woldemichael",descr="I Rock!")
 # artsadmin.objects.create(usersname='million',password='m1ll10n')
 #user = User.objects.create_user('million', 'million@gmail.com', 'm1ll10n')
 #artscategory.objects.create(category="tshirt",categorydescr="T-shirt")
 #artscategory.objects.create(category="bag", categorydescr="Hand bags")

 return redirect ("/")


