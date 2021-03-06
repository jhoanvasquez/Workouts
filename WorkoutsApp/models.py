from django.db import models

# Create your models here.

"""class Prueba (models.Model):
    descripcion = models.CharField(max_length = 20)
"""

class UserModel (models.Model):

    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    genero=models.CharField(max_length=20)
    email= models.EmailField()
    password=models.CharField(max_length=20)
    pais=models.CharField(max_length=20)
    region=models.CharField(max_length=20)
    ciudad=models.CharField(max_length=20)

class habilidadesUser (models.Model):
    user_id = models.ForeignKey(
        UserModel, on_delete=models.CASCADE)

    Resistencia = models.IntegerField()
    fuerza = models.IntegerField()
    velocidad = models.IntegerField()
    aceleración=models.IntegerField()
    Agilidad= models.IntegerField()
    flexibilidad = models.IntegerField()
    coordinación = models.IntegerField()
    precisión = models.IntegerField()
    