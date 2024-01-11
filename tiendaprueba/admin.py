from django.contrib import admin
from .models import Marca, Usuario, Producto, Compra

admin.site.register(Marca)
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Compra)