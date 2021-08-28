from django.contrib import admin
from .models import Planes
from .models import Usuarios
from .models import Areas, Rangos, Habilidades

# Register your models here.

admin.site.register(Planes)
admin.site.register(Usuarios)
admin.site.register(Areas)
admin.site.register(Rangos)
admin.site.register(Habilidades)