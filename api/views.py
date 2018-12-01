from django.shortcuts import render

#este paquete nos ayudara a 
#transformar arreglos de python
#en json
from django.core import serializers
from django.http import HttpResponse, HttpResponseBadRequest
import json
from core.models import *
# Create your views here.
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

def listar_personas(request):
    personas = Persona.objects.all()
    personaJson = serializers.serialize('json', personas)
    return HttpResponse(personaJson, content_type="application/json")

@csrf_exempt
@require_http_methods(['POST'])
def agregar_personas(request):
    body  = request.body.decode('utf-8')
    body_diccionario = json.loads(body)
    personas = Persona()
    personas.rut= body_diccionario['rut']
    personas.correo= body_diccionario['correo']
    personas.nombre= body_diccionario['nombre']     
    personas.fechaNac= body_diccionario['fechaNac']
    personas.phone= body_diccionario['phone']
    personas.region = Region(id=body_diccionario['region_id'])
    personas.ciudad = Ciudad(id=body_diccionario['ciudad_id'])
    personas.comuna = Comuna(id=body_diccionario['comuna_id'])
    personas.vivienda = Vivienda(id=body_diccionario['vivienda_id'])

    try:
        personas.save()
        mensaje = {
            'mensaje':'guardado correctamente'
        }
        return HttpResponse(json.dumps(mensaje), content_type="application/json")
    except:
        mensaje = {
            'mensaje':'error al guardar'
        }
        return HttpResponseBadRequest(json.dumps(mensaje), content_type="application/json") 
@csrf_exempt
@require_http_methods(['PUT'])
def modificar_personas(request):
    body  = request.body.decode('utf-8')
    body_diccionario = json.loads(body)
    personas = Persona()
    personas.rut = body_diccionario['rut']

    personas.correo= body_diccionario['correo']
    personas.nombre= body_diccionario['nombre']     
    personas.fechaNac= body_diccionario['fechaNac']
    personas.phone= body_diccionario['phone']
    personas.region = Region(id=body_diccionario['region_id'])
    personas.ciudad = Ciudad(id=body_diccionario['ciudad_id'])
    personas.comuna = Comuna(id=body_diccionario['comuna_id'])
    personas.vivienda = Vivienda(id=body_diccionario['vivienda_id'])

    try:
        personas.save()
        mensaje = {
            'mensaje':'modificado correctamente'
        }
        return HttpResponse(json.dumps(mensaje), content_type="application/json")
    except:
        mensaje = {
            'mensaje':'error al modificar'
        }
        return HttpResponseBadRequest(json.dumps(mensaje), content_type="application/json")
@csrf_exempt
@require_http_methods(['DELETE'])
def eliminar_personas(request, id):
    try:
        personas = Persona.objects.get(id=id)
        personas.delete()
        mensaje = {
            'mensaje':'Eliminado correctamente'
        }
        return HttpResponse(json.dumps(mensaje), content_type='application/json')
    except:
        mensaje = {
            'mensaje': 'No se ha podido eliminar'
        }
        return HttpResponseBadRequest(json.dumps(mensaje), content_type='application/json')

def listar_mascotas(request):
    mascotas = Mascota.objects.all()
    personaJson = serializers.serialize('json', mascotas)
    return HttpResponse(personaJson, content_type="application/json")

@csrf_exempt
@require_http_methods(['POST'])
def agregar_mascotas(request):
    body  = request.body.decode('utf-8')
    body_diccionario = json.loads(body)
    mascotas = Mascota()
    mascotas.chip= body_diccionario['chip']
    mascotas.nombre= body_diccionario['nombre']
    mascotas.raza = Raza(id=body_diccionario['raza_id'])     
    mascotas.sexo = Sexo(id=body_diccionario['sexo_id'])   
    mascotas.fechaI= body_diccionario['fechai']
    mascotas.fechaNac = body_diccionario['fechan']
    mascotas.descripcion = body_diccionario['descripcion']
    mascotas.imagen = Comuna(id=body_diccionario['imagen'])
    mascotas.estado = Estado(id=body_diccionario['estado_id'])

    try:
        mascotas.save()
        mensaje = {
            'mensaje':'guardado correctamente'
        }
        return HttpResponse(json.dumps(mensaje), content_type="application/json")
    except:
        mensaje = {
            'mensaje':'error al guardar'
        }
        return HttpResponseBadRequest(json.dumps(mensaje), content_type="application/json") 

@csrf_exempt
@require_http_methods(['PUT'])
def modificar_mascotas(request):
    body  = request.body.decode('utf-8')
    body_diccionario = json.loads(body)
    mascotas = Mascota()
    mascotas.chip = body_diccionario['chip']

    mascotas.nombre= body_diccionario['nombre']
    mascotas.raza = Raza(id=body_diccionario['raza_id'])     
    mascotas.sexo = Sexo(id=body_diccionario['sexo_id'])   
    mascotas.fechaI= body_diccionario['fechai']
    mascotas.fechaNac = body_diccionario['fechan']
    mascotas.descripcion = body_diccionario['descripcion']
    mascotas.imagen = Comuna(id=body_diccionario['imagen'])
    mascotas.estado = Estado(id=body_diccionario['estado_id'])

    try:
        mascotas.save()
        mensaje = {
            'mensaje':'modificado correctamente'
        }
        return HttpResponse(json.dumps(mensaje), content_type="application/json")
    except:
        mensaje = {
            'mensaje':'error al modificar'
        }
        return HttpResponseBadRequest(json.dumps(mensaje), content_type="application/json")

@csrf_exempt
@require_http_methods(['DELETE'])
def eliminar_mascotas(request, id):
    try:
        mascotas = Mascota.objects.get(id=id)
        mascotas.delete()
        mensaje = {
            'mensaje':'Eliminado correctamente'
        }
        return HttpResponse(json.dumps(mensaje), content_type='application/json')
    except:
        mensaje = {
            'mensaje': 'No se ha podido eliminar'
        }
        return HttpResponseBadRequest(json.dumps(mensaje), content_type='application/json')







    



