import email
from operator import mod
from django.db import models

# Create your models here.

class Usuarios(models.Model):
    usuario = models.CharField(max_length=40)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    correo = models.EmailField(max_length=40)
    password = models.CharField(max_length=50)
    cli = 1
    pro = 2
    eleccion = [(cli,'Cliente'),(pro,'Proveedor')]
    tipo = models.CharField(max_length=2, choices= eleccion,default=cli)

class Login_view(models.Model):
    usuario = models.CharField(max_length=40)
    password = models.CharField(max_length=50)
