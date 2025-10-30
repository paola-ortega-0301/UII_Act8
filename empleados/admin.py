# empleados/admin.py
from django.contrib import admin
from .models import Empleado

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido_paterno', 'telefono', 'correo', 'curp')
    search_fields = ('nombre', 'apellido_paterno', 'correo', 'curp')
    list_filter = ('apellido_paterno',) # Ejemplo de filtro