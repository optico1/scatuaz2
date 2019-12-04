from django.db import models

OPCIONES_SEXO = [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
]

OPCIONES_ESTADO_CIVIL = [
    ('S', 'Soltero'),
    ('C', 'Casado'),
]

OPCIONES_STATUS = [
    ('A', 'Activo'),
    ('I', 'Inactivo'),
]

# Create your models here.

class Trabajador(models.Model):

    nombre = models.CharField(max_length=100)
    paterno = models.CharField(max_length=100)
    materno = models.CharField(max_length=100)
    rfc = models.CharField(max_length=13, unique=True)
    curp = models.CharField(max_length=18, unique=True, null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=OPCIONES_SEXO, null=True, blank=True)
    estado_civil = models.CharField(max_length=1, choices=OPCIONES_ESTADO_CIVIL, null=True, blank=True)
    status = models.CharField(max_length=1, choices=OPCIONES_STATUS, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    pais_nacimiento = models.CharField(max_length=100, null=True, blank=True)
    estado_nacimiento = models.PositiveSmallIntegerField(null=True, blank=True)
    municipio_nacimiento = models.PositiveSmallIntegerField(null=True, blank=True)
    lugar_nacimiento = models.CharField(max_length=100, null=True, blank=True)
    pais_residencia = models.CharField(max_length=100, null=True, blank=True)
    estado_residencia = models.PositiveSmallIntegerField(null=True, blank=True)
    municipio_residencia = models.PositiveSmallIntegerField(null=True, blank=True)
    localidad_reside = models.CharField(max_length=100, null=True, blank=True)
    calle = models.CharField(max_length=100, null=True, blank=True)
    colonia = models.CharField(max_length=100, null=True, blank=True)
    cp = models.CharField(max_length=6, null=True, blank=True)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.paterno,self.materno,self.nombre

class Buscar(models.Model):
    pass