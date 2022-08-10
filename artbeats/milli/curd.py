from .entity.model import arts
from .entity.model import artsadmin
from django.shortcuts import render, redirect

def populate(self):
# arts.objects.create(title="Million Woldemichael",descr="I Rock!")
  artsadmin.objects.create(usersname='million',password='m1ll10n')
  return redirect ("/")

