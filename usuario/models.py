from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Genero(models.Model):
    detalleGenero = models.CharField(max_length=9)


class Perfil(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    edad = models.IntegerField()
    fNacimiento = models.DateField()
    genero = models.ForeignKey(Genero,on_delete=models.CASCADE)
    usuario= models.OneToOneField(User,on_delete=models.CASCADE)

