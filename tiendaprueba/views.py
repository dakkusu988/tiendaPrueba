from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, View
from .models import Producto
from django.urls import reverse, reverse_lazy
from typing import Any
from datetime import date
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

# 1. TIENDA (CRUD)
class listadoProductos(ListView):
    model = Producto
    template_name = 'tiendaprueba/listadoProductos.html'


class anadirProductos(CreateView):
    model = Producto
    fields = ['nombre', 'modelo', 'unidades', 'precio', 'VIP_producto', 'marca_producto']
    template_name = "tiendaprueba/anadirProductos.html"

    # Puedes redirigir a una vista específica usando reverse
    def get_success_url(self):
        return reverse('listadoProductos')

class detallesProductos(DetailView):
    model = Producto
    template_name = 'tiendaprueba/detallesProductos.html'
    