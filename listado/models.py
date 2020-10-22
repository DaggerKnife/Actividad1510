from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Producto(models.Model):
    nombreProducto = models.CharField(max_length=64)
    precioProducto = models.IntegerField()

class DetalleListado(models.Model):
    idProducto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidadProducto = models.IntegerField()

class Listado(models.Model):
    usuario= models.ForeignKey(User,on_delete=models.CASCADE)

    


