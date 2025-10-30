# empleados/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_empleados, name='lista_empleados'), # /empleados/
    path('nuevo/', views.crear_empleado, name='crear_empleado'), # /empleados/nuevo/
    path('editar/<int:pk>/', views.editar_empleado, name='editar_empleado'), # /empleados/editar/1/
    path('eliminar/<int:pk>/', views.eliminar_empleado, name='eliminar_empleado'), # /empleados/eliminar/1/
]