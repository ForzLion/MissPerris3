from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('galeria/', galeria, name='galeria'),
    path('formulario/', formulario, name='formulario'),   
    path('formulario_mascota/',  formulario_mascota ,name='formulario_mascota'),
    path('listar_mascotas/',  listar_mascotas ,name='listarM'),
    path('listar_personas/',  listar_personas ,name='listarP'), 
    path('eliminarP/<id>/', eliminar_personas, name="eliminar"),
    path('modificarP/<id>/', modificar_personas, name="modificar"),
    path('eliminarM/<id>/', eliminar_mascotas, name="eliminarM"),
    path('modificarM/<id>/', modificar_mascota, name="modificarM"),
    
    

]