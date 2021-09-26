from django.contrib import admin
from .models import Planes
from .models import Usuarios
from .models import Areas, Rangos, Habilidades, Ejercicios, Sesion_Ejercicio, Sesiones

# Register your models here.
class AreaAdmin(admin.ModelAdmin):
    list_display = ('id_area', 'descripcion')

class EjerciciosAdmin(admin.ModelAdmin):
    list_display = ('id_ejercicios','descripcion', 'duracion', 'explicacion', 'id_area', 'id_rango')

class SesionesAdmin(admin.ModelAdmin):
    list_display = ('id_sesion','id_plan')

admin.site.register(Planes)
admin.site.register(Usuarios)
admin.site.register(Areas, AreaAdmin)
admin.site.register(Rangos)
admin.site.register(Habilidades)
admin.site.register(Sesion_Ejercicio)
admin.site.register(Ejercicios, EjerciciosAdmin)
admin.site.register(Sesiones, SesionesAdmin)
