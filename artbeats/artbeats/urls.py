from django.contrib import admin
from django.urls import include, path
from milli import views
from milli import aleka
from milli import curd
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index, name='index'),
    path(r'^$', include('milli.urls')),
    path('astedadari/', include('milli.urls')),
    path('aleka/',aleka.index, name='index'),
    path('login/',aleka.login,name='login'),
    path('logout/',aleka.logout,name='logout'),
    path('save/',aleka.save,name='save'),
    path('curd/',curd.populate,name='curd'),
    path('alekaw/',include('milli.urls')),
    path('admin/', admin.site.urls),
]