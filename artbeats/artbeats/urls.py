from django.contrib import admin
from django.urls import include, path
from milli import views
from milli import aleka
from milli import curd
from milli import pagesetup
from milli import products
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index, name='index'),
    path(r'^$', include('milli.urls')),
    path('astedadari/', include('milli.urls')),
    path('aleka/',aleka.index, name='index'),
    path('aleka/products',products.index, name='index'),
    path('aleka/addproducts',products.add,name='add'),
    path('aleka/saveproducts',products.save,name='save'),
    path('aleka/products/remove/',products.remove,name='remove'),
    path('aleka/editproduct',products.edit,name='edit'),
    path('aleka/updaterecord/',products.updaterecord,name='updaterecord'),
    path('aleka/pagesetup',pagesetup.index,name='index'),
    path('userlogin/',aleka.userlogin,name='userlogin'),
    path('userlogout/', aleka.userlogout, name='userlogout'),
    path('logout/',aleka.logout,name='logout'),
    path('save/',aleka.save,name='save'),
    path('curd/',curd.populate,name='curd'),
    path('alekaw/',include('milli.urls')),
    path('admin/', admin.site.urls),
]