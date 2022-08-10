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

