# empleados/forms.py
from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__' # Incluye todos los campos del modelo
        # O puedes especificar:
        # fields = ['nombre', 'apellido_paterno', 'apellido_materno', 'telefono', 'correo', 'curp']

        widgets = { # Opcional: Personaliza la apariencia de los campos
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre(s)'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido Paterno'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido Materno'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 5512345678'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@dominio.com'}),
            'curp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CURP'}),
        }