from django.contrib import admin
from .models import *


class PersonaAdmin(admin.ModelAdmin):
    list_display=('rut','correo','nombre','fechaNac','phone','region','ciudad','comuna','vivienda')
    search_fields=['rut','nombre']
    list_filter=('comuna',)
    
#class MascotaAdmin(admin.ModelAdmin):
   # list_display=('chip','nombre','raza','sexo','fechaI','fechaNac','descripcion','imagen','estado')
  #  search_fields=['chip','nombre']
   # list_filter=('raza',)
    

  
 
admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Comuna)
admin.site.register(Vivienda)
admin.site.register(Persona,PersonaAdmin)
admin.site.register(Raza)
admin.site.register(Estado)
admin.site.register(Mascota)
admin.site.register(Sexo)