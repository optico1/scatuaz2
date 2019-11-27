from django.db import models

# Create your models here.

class Trabajador(models.Model):
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

    nombre = models.CharField(max_length=100)
    paterno = models.CharField(max_length=100)
    materno = models.CharField(max_length=100)
    rfc = models.CharField(max_length=13, unique=True)
    curp = models.CharField(max_length=18, unique=True)
    sexo = models.CharField(max_length=1, choices=OPCIONES_SEXO)
    estado_civil = models.CharField(max_length=1, choices=OPCIONES_ESTADO_CIVIL)
    status = models.CharField(max_length=1, choices=OPCIONES_STATUS)
    fecha_nacimiento = models.DateField()
    pais_nacimiento = models.CharField(max_length=100)
    estado_nacimiento = models.PositiveSmallIntegerField()
    municipio_nacimiento = models.PositiveSmallIntegerField()
    lugar_nacimiento = models.CharField(max_length=100)
    pais_residencia = models.CharField(max_length=100)
    estado_residencia = models.PositiveSmallIntegerField()
    municipio_residencia = models.PositiveSmallIntegerField()
    localidad_reside = models.CharField(max_length=100)
    calle = models.CharField(max_length=100)
    colonia = models.CharField(max_length=100)
    cp = models.CharField(max_length=6)
    telefono = models.CharField(max_length=10)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.paterno,self.materno,self.nombre

class Buscar(models.Model):
    pass