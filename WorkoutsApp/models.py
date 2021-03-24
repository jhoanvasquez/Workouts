from django.db import models


class Rangos(models.Model):
    id_habilidad=models.IntegerField()
    nivel_habilidad=models.IntegerField()

class Areas(models.Model):
    id_area=models.IntegerField()
    descripcion=models.CharField(max_length=150)
    links=models.CharField(max_length=150)
    sesiones=models.CharField(max_length=50)

class Ejercicios(models.Model):
    id_ejercicios=models.IntegerField()
    descripcion=models.CharField(max_length=150)
    id_habilidad=models.ForeignKey(Rangos, on_delete=models.CASCADE)
    duracion=models.IntegerField()
    explicacion=models.CharField(max_length=150)


class Usuarios (models.Model):
    id_usuario=models.IntegerField()
    nombre=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=50)
    edad=models.IntegerField()
    peso=models.CharField(max_length=3)
    estatura=models.CharField(max_length=3)
    correo=models.EmailField()
    contra=models.CharField(max_length=15)
    ciudad=models.CharField(max_length=50)
    puntajehabilidad=models.IntegerField()
    id_habilidad=models.ForeignKey(Rangos, on_delete=models.CASCADE )

    #idhabilidad=models.ForeignKey(Rangos, blank=True, null=True)


class Planes(models.Model):
    id_plan=models.IntegerField()
    id_area=models.ForeignKey(Areas, on_delete=models.CASCADE )
    id_usuario=models.ForeignKey(Usuarios, on_delete=models.CASCADE )
    id_ejercicios=models.ForeignKey(Ejercicios, on_delete=models.CASCADE )
    id_habilidad=models.ForeignKey(Rangos, on_delete=models.CASCADE )
    diasdisponibles=models.IntegerField()
    diasentrenados=models.IntegerField()
    dias_esta_semana=models.IntegerField()
    """ fecha=models.DateField()
    entrenehoy=models.BooleanField() """
    
