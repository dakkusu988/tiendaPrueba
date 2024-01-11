from django import forms
from .models import Producto

class LibroForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'modelo', 'unidades', 'precio', 'VIP_producto', 'marca_producto']