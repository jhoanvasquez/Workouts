from django.contrib import admin
from .models import Planes
from .models import Usuarios
from .models import Areas, Rangos, Habilidades, Ejercicios, Sesion_Ejercicio, Sesiones

# Register your models here.
class AreaAdmin(admin.ModelAdmin):
    list_display = ('id_area', 'descripcion')

class EjerciciosAdmin(admin.ModelAdmin):
    list_display = ('id_ejercicios','descripcion','id_rango','duracion','repeticiones','calificacion','explicacion','id_area','link_entreno')

class PlanesAdmin(admin.ModelAdmin):
    list_display = ('id_plan','id_area','id_usuario','id_rango','dias_disponibles','dias_entrenados','dias_esta_semana','num_sesiones','ultima_semana')

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'fk_user', 'edad', 'peso', 'estatura', 'ciudad', 'puntaje_habilidades', 'id_rango')

class RangosAdmin(admin.ModelAdmin):
    list_display = ('id_rango','descripcion')

class HabilidadesAdmin(admin.ModelAdmin):
    list_display = ('id_habilidades','flexibilidad','fuerza','resistencia','velocidad','aceleracion','agilidad','coordinacion','precision','fk_user','id_rango')

class SesionesAdmin(admin.ModelAdmin):
    list_display = ('id_sesion','id_plan','fecha','num_sesiones')

class Sesion_EjercicioAdmin(admin.ModelAdmin):
    list_display = ('id','id_sesion','id_ejercicios')


admin.site.register(Planes, PlanesAdmin)
admin.site.register(Usuarios, UsuariosAdmin)
admin.site.register(Areas, AreaAdmin)
admin.site.register(Rangos, RangosAdmin)
admin.site.register(Habilidades, HabilidadesAdmin)
admin.site.register(Ejercicios, EjerciciosAdmin)
admin.site.register(Sesion_Ejercicio, Sesion_EjercicioAdmin)
admin.site.register(Sesiones, SesionesAdmin)

