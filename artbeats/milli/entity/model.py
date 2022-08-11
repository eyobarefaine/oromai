from django.db import models
from django.contrib.auth.models import UserManager
class arts(models.Model):
    title = models.CharField(max_length=128)
    descr = models.CharField(max_length=250)


    def __str__(self):
        return self.title
    def publish (self,title,descr):
        obj = arts.objects.first()
        arts.save(obj,title,descr)


class artsadmin(models.Model):
    usersname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class artsproducts(models.Model):
    artsname = models.CharField(max_length=128)
    artsdescr = models.CharField(max_length=256)
    artspath = models.CharField(max_length=300)
    artsprice = models.DecimalField(max_digits=6, decimal_places=2)
    artscatagory = models.CharField(max_length=15)

class artscategory(models.Model):
    category = models.CharField(max_length=50)
    categorydescr = models.CharField(max_length=50)


