from django.db import models
from django.contrib.auth.models import AbstractUser

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Usuario(AbstractUser):
    VIP_usuario = models.BooleanField()
    saldo = models.CharField(max_length=255)

    # Agregar related_name para evitar conflictos con auth.User
    groups = models.ManyToManyField("auth.Group", related_name="usuarios")
    user_permissions = models.ManyToManyField("auth.Permission", related_name="usuarios_permissions")

    def __str__(self):
        return self.username

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    modelo = models.CharField(max_length=255)
    unidades = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    VIP_producto = models.BooleanField()
    marca_producto = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Compra(models.Model):
    usuario_comprador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateField()
    unidades = models.PositiveIntegerField(null=True, blank=True)
    importe = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    IVA = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    producto_comprado = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.usuario_comprador.username} - {self.producto_comprado.nombre}'