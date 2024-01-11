# Archivo urls.py de tiendaprueba

from django.urls import path
from .views import listadoProductos, anadirProductos, detallesProductos

urlpatterns = [
    path('', listadoProductos.as_view(), name='listadoProductos'),
    path('anadir', anadirProductos.as_view(), name='anadirProductos'),
    path('detalles/<int:pk>', detallesProductos.as_view(), name='detallesProductos'),
]
