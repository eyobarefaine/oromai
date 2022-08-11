from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.shortcuts import render, redirect
from .entity.model import arts

@login_required(login_url='/userlogin')
def index(request):
        obj = arts.objects.first()
        title = getattr(obj, 'title')
        descr = getattr(obj, 'descr')
        my = loader.get_template('alekapagesetup.html')
        context = {
            'title': 'Milli Artbeats Page', 'artist': 'Admins', 'title': title, 'descr': descr
        }
        return HttpResponse(my.render(context, request))

