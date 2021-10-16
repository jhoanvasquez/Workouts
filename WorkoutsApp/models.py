from django.contrib.auth.models import User
from django.db import models


class Rangos(models.Model):
    id_rango=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=150)
    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)

class Areas(models.Model):
    
    id_area=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=150)
    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)

class Ejercicios(models.Model):
    id_ejercicios=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=150)
    id_rango=models.ForeignKey(Rangos, on_delete=models.CASCADE)
    duracion=models.IntegerField()
    repeticiones=models.IntegerField()
    calificacion=models.IntegerField()
    explicacion=models.CharField(max_length=150)
    id_area=models.ForeignKey(Areas, on_delete=models.CASCADE)
    link_entreno=models.CharField(max_length=150)

class Usuarios (models.Model):
    id_usuario=models.AutoField(primary_key=True)
    fk_user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    edad=models.IntegerField()
    peso=models.CharField(max_length=4)
    estatura=models.CharField(max_length=4)
    ciudad=models.CharField(max_length=50)
    puntaje_habilidades=models.IntegerField()
    id_rango=models.ForeignKey(Rangos, on_delete=models.CASCADE)

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)

class EjerciciosUsuarios(models.Model):
    id_ejercicios_usuarios=models.AutoField(primary_key=True)
    id_ejercicios=models.ForeignKey(Ejercicios, on_delete=models.CASCADE)   #!fk ejercicios
    descripcion=models.CharField(max_length=150)
    id_rango=models.ForeignKey(Rangos, on_delete=models.CASCADE)
    duracion=models.IntegerField()
    repeticiones=models.IntegerField()
    calificacion=models.IntegerField()
    explicacion=models.CharField(max_length=150)
    id_area=models.ForeignKey(Areas, on_delete=models.CASCADE)
    link_entreno=models.CharField(max_length=150)
    id_usuario=models.ForeignKey(Usuarios, on_delete=models.CASCADE)   #!fk id usuarios

class Planes(models.Model):
    id_plan=models.AutoField(primary_key=True)
    id_area=models.ForeignKey(Areas, on_delete=models.CASCADE )
    id_usuario=models.ForeignKey(Usuarios, on_delete=models.CASCADE )
    id_rango=models.ForeignKey(Rangos, on_delete=models.CASCADE )
    dias_disponibles=models.IntegerField()
    dias_entrenados=models.IntegerField()
    dias_esta_semana=models.IntegerField()
    num_sesiones=models.IntegerField()
    ultima_semana=models.DateField()

class Sesiones(models.Model):
    id_sesion=models.AutoField(primary_key=True)
    id_plan=models.ForeignKey(Planes, on_delete=models.CASCADE )
    fecha=models.DateField()
    num_sesiones=models.IntegerField()

class Sesion_Ejercicio(models.Model):
    id = models.AutoField(primary_key=True)
    id_sesion=models.ForeignKey(Sesiones, on_delete=models.CASCADE )
    id_ejercicios=models.ForeignKey(Ejercicios, on_delete=models.CASCADE )
    calificacion=models.IntegerField(null=True, blank=True)
    mejor_sesion=models.IntegerField(null=True, blank=True)
    fecha=models.DateField()

class Habilidades(models.Model):
    id_habilidades=models.AutoField(primary_key=True)
    flexibilidad=models.IntegerField()
    fuerza=models.IntegerField()
    resistencia=models.IntegerField()
    velocidad=models.IntegerField()
    aceleracion=models.IntegerField()
    agilidad=models.IntegerField()
    coordinacion=models.IntegerField()
    precision=models.IntegerField()
    fk_user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    id_rango=models.ForeignKey(Rangos, on_delete=models.CASCADE )

    
