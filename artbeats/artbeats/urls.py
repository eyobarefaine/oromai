from django.contrib import admin
from django.urls import include, path
from milli import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('/',views.index, name='index'),
    path(r'^$', include('milli.urls')),
    path('astedadari/', include('milli.urls')),
    path('aleka/',include('milli.urls')),
    path('alekaw/',include('milli.urls')),
    path('admin/', admin.site.urls),
]