from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path('milli/', include('milli.urls')),
    path('admin/', admin.site.urls),
]