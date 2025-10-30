# empleados/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado
from .forms import EmpleadoForm

# READ: Listar todos los empleados
def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/lista_empleados.html', {'empleados': empleados})

# CREATE: Crear un nuevo empleado
def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados') # Redirige a la lista después de guardar
    else:
        form = EmpleadoForm()
    return render(request, 'empleados/empleado_form.html', {'form': form, 'titulo': 'Crear Empleado'})

# UPDATE: Actualizar un empleado existente
def editar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk) # Obtiene el empleado o devuelve 404
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado) # Pasa la instancia para actualizarla
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = EmpleadoForm(instance=empleado) # Carga los datos existentes en el formulario
    return render(request, 'empleados/empleado_form.html', {'form': form, 'titulo': 'Editar Empleado'})

# DELETE: Eliminar un empleado
def eliminar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST': # Se suele hacer con un POST para confirmar la eliminación
        empleado.delete()
        return redirect('lista_empleados')
    return render(request, 'empleados/confirmar_eliminar.html', {'empleado': empleado})