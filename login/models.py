from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    correo = models.CharField(max_length=100)
    usuario = models.OneToOneField(User,verbose_name="Usuario",on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_usuario
