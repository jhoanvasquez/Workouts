from django.contrib import admin
from .models import Ejercicios, Planes, Usuarios, Areas, Rangos, Habilidades, Sesiones, Sesion_Ejercicio

# Register your models here.

admin.site.register(Planes)
admin.site.register(Usuarios)
admin.site.register(Areas)
admin.site.register(Rangos)
admin.site.register(Habilidades)
admin.site.register(Ejercicios)
admin.site.register(Sesiones)
admin.site.register(Sesion_Ejercicio)
