# empleados/models.py
from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100, blank=True, null=True) # blank=True para formularios, null=True para la DB
    telefono = models.CharField(max_length=20, unique=True)
    correo = models.EmailField(max_length=150, unique=True)
    curp = models.CharField(max_length=18, unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno}"

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ['apellido_paterno', 'nombre'] # Ordena por defecto