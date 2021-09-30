from django.db import models

# Create your models here.

class cliente(models.Model):
    pk_cliente = models.AutoField(primary_key=True, blank=False, null=False)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    telefono=models.CharField(max_length=8, blank=False, null=False)
    direccion = models.TextField(blank=False, null=False)

class mascota(models.Model):
    pk_mascota = models.AutoField(primary_key=True, blank=False, null=False)
    nombremasc = models.CharField(max_length=50, blank=False, null=False)
    raza = models.CharField(max_length=50, blank=False, null=False)
    edad = models.CharField(max_length=2, blank=False, null=False)

