from django.urls import path
from . import views
from . import aleka

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.astedadari, name='astedadari'),
    path('', aleka.index,name='index')

]