# Archivo urls.py de mysite

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('tiendaprueba.urls')),
]