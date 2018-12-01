from django.db import models
class Region(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=200)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name="Region"        
        verbose_name_plural="Regiones"        
class Comuna(models.Model):
     nombre=models.CharField(max_length=50)
     descripcion=models.CharField(max_length=200)
     def __str__(self):
        return self.nombre
     class Meta:
        verbose_name="Comuna"    
        verbose_name_plural="Comunas"    
class Ciudad(models.Model):
     nombre=models.CharField(max_length=50)
     descripcion=models.CharField(max_length=200)
     def __str__(self):
        return self.nombre
     class Meta:
        verbose_name="Ciudad"    
        verbose_name_plural="Ciudades"    

class Vivienda(models.Model):
     nombre=models.CharField(max_length=50)
     descripcion=models.CharField(max_length=200)
     def __str__(self):
        return self.nombre
     class Meta:
        verbose_name="Vivienda"    
        verbose_name_plural="Viviendas"    
class Persona(models.Model):
    rut=models.CharField(max_length=50,unique=True)
    correo=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    fechaNac=models.DateField()
    phone=models.IntegerField()
    region=models.ForeignKey(Region,on_delete=models.CASCADE)
    comuna=models.ForeignKey(Comuna,on_delete=models.CASCADE)
    ciudad=models.ForeignKey(Ciudad,on_delete=models.CASCADE)
    vivienda=models.ForeignKey(Vivienda,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name="persona"    
        verbose_name_plural="personas"  

 
class Raza(models.Model):
     nombre=models.CharField(max_length=50)
     descripcion=models.CharField(max_length=200)
     def __str__(self):
        return self.nombre
     class Meta:
        verbose_name="Raza"    
        verbose_name_plural="Razas"    

class Estado(models.Model):
     nombre=models.CharField(max_length=50)
     descripcion=models.CharField(max_length=200)
     def __str__(self):
        return self.nombre
     class Meta:
        verbose_name="Estado"    
        verbose_name_plural="Estados"    

class Sexo(models.Model):
     nombre=models.CharField(max_length=50)
     descripcion=models.CharField(max_length=200)
     def __str__(self):
        return self.nombre
     class Meta:
        verbose_name="Sexo"    
        verbose_name_plural="Sexos"
       
class Mascota(models.Model):
    chip=models.IntegerField(unique=True)
    nombre=models.CharField(max_length=50)
    raza=models.ForeignKey(Raza,on_delete=models.CASCADE)
    sexo=models.ForeignKey(Sexo,on_delete=models.CASCADE)
    fechaI=models.DateField()
    fechaNac=models.DateField()
    descripcion=models.TextField(max_length=300)
    imagen=models.ImageField(upload_to='mascotas')
    estado=models.ForeignKey(Estado,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name="Mascota"    
        verbose_name_plural="Mascotas"             
        