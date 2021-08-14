from django.contrib.auth.models import User
from django.db import models


class Rangos(models.Model):
    id_rango=models.IntegerField()
    descripcion=models.CharField(max_length=150)

class Areas(models.Model):
    id_area=models.IntegerField()
    descripcion=models.CharField(max_length=150)


class Ejercicios(models.Model):
    id_ejercicios=models.IntegerField()
    descripcion=models.CharField(max_length=150)
    id_rango=models.ForeignKey(Rangos, on_delete=models.CASCADE)
    duracion=models.IntegerField()
    explicacion=models.CharField(max_length=150)
    id_area=models.ForeignKey(Areas, on_delete=models.CASCADE)
    link_entreno=models.CharField(max_length=150)


class Usuarios (models.Model):
    fk_user = models.OneToOneField(User, on_delete=models.CASCADE)
    #id_usuario=models.IntegerField()
    #nombre=models.CharField(max_length=30)
    #apellidos=models.CharField(max_length=50)
    edad=models.IntegerField()
    peso=models.CharField(max_length=3)
    estatura=models.CharField(max_length=3)
    #correo=models.EmailField()
    #contra=models.CharField(max_length=15)
    ciudad=models.CharField(max_length=50)
    puntaje_habilidades=models.IntegerField()
    id_rango=models.ForeignKey(Rangos, on_delete=models.CASCADE)

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)

    #idhabilidad=models.ForeignKey(Rangos, blank=True, null=True)


class Planes(models.Model):
    id_plan=models.IntegerField()
    id_area=models.ForeignKey(Areas, on_delete=models.CASCADE )
    id_usuario=models.ForeignKey(Usuarios, on_delete=models.CASCADE )
    id_rango=models.ForeignKey(Rangos, on_delete=models.CASCADE )
    dias_disponibles=models.IntegerField()
    dias_entrenados=models.IntegerField()
    dias_esta_semana=models.IntegerField()
    num_sesiones=models.IntegerField()
    ultima_semana=models.DateField()

    "entrenehoy=models.BooleanField() "

class Sesiones(models.Model):
    id_sesion=models.IntegerField()
    id_plan=models.ForeignKey(Planes, on_delete=models.CASCADE )
    fecha=models.DateField()

class Sesion_Ejercicio(models.Model):
    id_sesion=models.ForeignKey(Sesiones, on_delete=models.CASCADE )
    id_ejercicios=models.ForeignKey(Ejercicios, on_delete=models.CASCADE )
    

class Habilidades(models.Model):
    id_habilidades=models.IntegerField()
    flexibilidad=models.IntegerField()
    fuerza=models.IntegerField()
    resistencia=models.IntegerField()
    velocidad=models.IntegerField()
    aceleracion=models.IntegerField()
    agilidad=models.IntegerField()
    coordinacion=models.IntegerField()
    precision=models.IntegerField()
    id_usuario=models.ForeignKey(Usuarios, on_delete=models.CASCADE )
    id_rango=models.ForeignKey(Rangos, on_delete=models.CASCADE )
    
