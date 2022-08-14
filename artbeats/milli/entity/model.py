from django.db import models
from django.contrib.auth.models import UserManager
#eyobwoldemichael   
class arts(models.Model):
    title = models.TextField(default='')
    descr = models.TextField(default='')


    def __str__(self):
        return self.title
    def publish (self,title,descr):
        obj = arts.objects.first()
        arts.save(obj,title,descr)


class artsadmin(models.Model):
    usersname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class artsproducts(models.Model):
    products = models.TextField(default=' ')

class artbeatproducts(models.Model):
    artsimage = models.ImageField(upload_to='static/milli/img')
    artsname = models.TextField(default='')
    artsdescr = models.TextField( default=' ')
    artspath = models.TextField( default=' ')
    artsprice = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    artscatagory = models.TextField( default=' ')
    artsmis   = models.TextField(default=' ')


class artscategory(models.Model):
    category = models.CharField(max_length=50)
    categorydescr = models.CharField(max_length=50)


