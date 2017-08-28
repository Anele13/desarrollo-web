from __future__ import unicode_literals
from django.db import models
from .choices import *
from django.contrib.auth.models import AbstractUser, Group
from liquidacion.models import Empresa

class Rol(models.Model):
    class Meta:
        abstract= True


class Agente(Rol):
     def get_view_name(self):
        return "Agente"


class Administrador(Rol):
    saf= models.ForeignKey(Empresa,blank=True, null=True, on_delete=models.CASCADE)

    def get_saf():
        return self.saf


class Usuario(Rol, AbstractUser):
    AGENTE = "AGENTE"
    ADMINISTRADOR = "ADMINISTRADOR"

    def get_view_name(self):
        return self.groups.first().name

    def get_view_groups(self):
        return self.groups.all()


class Persona(models.Model):
    documento  = models.BigIntegerField()
    tipo_doc = models.CharField(max_length=10, choices=Tipo)
    agente= models.OneToOneField(Agente, blank=True, null=True, on_delete=models.CASCADE)
    administrador= models.OneToOneField(Administrador, blank=True, null=True, on_delete=models.CASCADE)
    usuario = models.OneToOneField(Usuario, blank=True, null=True, on_delete=models.CASCADE)


class Direccion(models.Model):
    provincia = models.IntegerField()
    cp = models.CharField(max_length=8)
    localidad = models.CharField(max_length=60)
    calle = models.CharField(max_length=40)
    nro = models.CharField(max_length=6)
    piso = models.CharField(max_length=5, null=True, blank=True)
    dpto = models.CharField(max_length=5, null = True, blank=True )
    extra= models.CharField(max_length=5)
