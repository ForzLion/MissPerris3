from django.urls import path
from .views import *

urlpatterns = [
    path('personas/', listar_personas, name="api_listar_personas"),
    path('personas/agregar/', agregar_personas, name="api_agregar_auto"),
    path('personas/modificar/', modificar_personas, name="api_modificar_personas"),
    path('personas/<id>/eliminar/', eliminar_personas, name="api_eliminar_personas"),
    path('mascotas/', listar_mascotas, name="api_listar_mascotas"),
    path('mascotas/agregar/', agregar_mascotas, name="api_agregar_mascotas"),
    path('mascotas/modificar/', modificar_mascotas, name="api_modificar_mascotas"),
    path('mascotas/<id>/eliminar/', eliminar_mascotas, name="api_eliminar_mascotas"),



]