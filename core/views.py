from django.shortcuts import render,redirect    
from .models import *
from django.conf import settings

from django.conf.urls.static import static

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django_xhtml2pdf.utils import pdf_decorator

# Create your views here.
def home(request):
    return render(request,'core/home.html')


@login_required
def formulario(request):
    regiones=Region.objects.all()
    ciudades=Ciudad.objects.all()
    comunas=Comuna.objects.all()
    viviendas=Vivienda.objects.all()
    variables={
        'regiones':regiones,
        'ciudades':ciudades,
        'comunas':comunas,
        'viviendas':viviendas
       


    }

    if request.POST:
        persona=Persona()
        persona.rut=request.POST.get('txtRun')
        persona.correo=request.POST.get('txtCorreo')
        persona.nombre=request.POST.get('txtNombre')        
        persona.fechaNac=request.POST.get('txtFechaN')
        persona.phone=request.POST.get('txtTelefono')

        region=Region() 
        region.id= int(request.POST.get('cboRegion'))
        persona.region = region 
        ciudad = Ciudad()
        ciudad.id = int(request.POST.get('cboCiudad'))
        persona.ciudad=ciudad
        comuna = Comuna()
        comuna.id = int(request.POST.get('cboComuna'))   
        persona.comuna=comuna
         
       
        vivienda=Vivienda()
        vivienda.id= int(request.POST.get('cboVivienda'))   
        persona.vivienda=vivienda
       
  
       
        try:
            persona.save()
            variables['mensaje']="Guardado Correctamente"
        except:
            variables['mensaje'] ="No se ha podido guardar "   



    return render(request,'core/formulario.html',variables)


@login_required
def formulario_mascota(request):
    razas=Raza.objects.all()
    estados=Estado.objects.all()
    sexos=Sexo.objects.all()
    variables={
        
        'razas':razas,
        'estados':estados,
        'sexos':sexos
    
    }

    if request.POST:
        mascota=Mascota()
        mascota.chip=request.POST.get('txtchip')
        mascota.nombre=request.POST.get('txtNombreM')
        raza=Raza() 
        raza.id= int(request.POST.get('cboRaza'))
        mascota.raza=raza                     
        sexo=Sexo()
        sexo.id=int(request.POST.get('cboSexo')) 
        mascota.sexo=sexo
        mascota.fechaI=request.POST.get('txtFechaI')
        mascota.fechaNac=request.POST.get('txtFechaN')
        mascota.descripcion=request.POST.get('txtDescripcion')      
        mascota.imagen=request.FILES.get('imgMascota') 
        estado=Estado()
        estado.id= int(request.POST.get('cboEstado'))   
        mascota.estado=estado
       
  
       
       

        try:
            mascota.save()
            variables['mensaje']=" Mascota Guardada Correctamente"
        except:
            variables['mensaje'] ="No se ha podido guardar  la Mascota"   


    return render(request,'core/formulario_mascota.html',variables)




    
 
def listar_personas(request):
    personas=Persona.objects.all()

    return render(request, 'core/listar_personas.html',{
        'personas':personas})
    

def eliminar_personas(request,id):
        persona=Persona.objects.get(id=id)
        try:
            persona.delete()
            mensaje="Se elimino correctamente"
            messages.success(request,mensaje)
        except:
            mensaje="No se elimino correctamente"
            messages.error(request,mensaje)
        
        return redirect(to='listarP')



def modificar_personas(request,id):
   
    regiones=Region.objects.all()
    ciudades=Ciudad.objects.all()
    comunas=Comuna.objects.all()
    viviendas=Vivienda.objects.all()
    persona=Persona.objects.get(id=id)
    variables= {
     'persona':persona,
     'regiones':regiones,
     'ciudades':ciudades,
     'comunas':comunas,
      'viviendas':viviendas
    }
    if request.POST:
        persona = Persona()
        persona.id = request.POST.get('txtId')
        persona.rut = request.POST.get('txtRun')
        persona.correo = request.POST.get('txtCorreo')
        persona.nombre = request.POST.get('txtNombre')        
        persona.fechaNac = request.POST.get('txtFechaN')
        persona.phone = request.POST.get('txtTelefono')

        region = Region() 
        region.id = int(request.POST.get('cboRegion'))
        persona.region = region 
        ciudad = Ciudad()
        ciudad.id = int(request.POST.get('cboCiudad'))
        persona.ciudad = ciudad
        comuna = Comuna()
        comuna.id = int(request.POST.get('cboComuna'))   
        persona.comuna = comuna
        vivienda = Vivienda()
        vivienda.id = int(request.POST.get('cboVivienda'))   
        persona.vivienda = vivienda
       
  
       
       
        
        
        

        try:
             persona.save()
             messages.success(request,"Guardado Correctamente")
        except:
             messages.error(request,"No se ha podido guardar")
        return redirect('listarP')   


    
    return render(request,'core/modificar_personas.html',variables)

 










def listar_mascotas(request):
    mascotas=Mascota.objects.all()

    return render(request,'core/listar_mascotas.html',{
        'mascotas':mascotas
    })



    

def eliminar_mascotas(request,id):
        mascota=Mascota.objects.get(id=id)
        try:
            mascota.delete()
            mensaje="Se elimino correctamente"
            messages.success(request,mensaje)
        except:
            mensaje="No se elimino correctamente"
            messages.error(request,mensaje)
        
        return redirect(to='listarM')





def  modificar_mascota(request,id):
    razas=Raza.objects.all()
    estados=Estado.objects.all()
    mascota= Mascota.objects.get(id=id)
    variables={
        
        'razas':razas,
        'estados':estados
    
    }

    if request.POST:
        mascota=Mascota()
        mascota.chip=request.POST.get('txtchip')
        mascota.nombre=request.POST.get('txtNombreM')
        raza=Raza() 
        raza.id= int(request.POST.get('cboRaza'))
        mascota.raza=raza                     
        mascota.sexo=request.Post.get('rbtSexo')   
        mascota.fechaI=request.POST.get('txtFechaI')
        mascota.fechaNac=request.POST.get('txtFechaN')
        mascota.descripcion=request.POST.get('txtDescripcion')      
        mascota.imagen=request.POST.get('imgMascota') 
        estado=Estado()
        estado.id= int(request.POST.get('cboEstado'))   
        mascota.estado=estado
       
  
       
       
        
        
        

        try:
            mascota.save()
            variables['mensaje']=" Mascota modificada Correctamente"
        except:
            variables['mensaje'] ="No se ha podido modificar  la Mascota"   
        return redirect('listarM')

    return render(request,'core/formulario_mascota.html',variables)


def galeria(request):
    return render(request,'core/galeria.html')





    