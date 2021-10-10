from django.contrib import admin
from django.urls import path

from WorkoutsApp import views
from . import views

app_name = 'workoutsapp'

urlpatterns = [

    #path('admin/', admin.site.urls), 
    path('register/', views.register, name="register"),
    path('sesion0/<int:id>', views.sesion0, name='sesion0'),
    path('dashboard/<int:id>', views.dashboard, name="dashboard"),
    path('aumentasesion/<int:id>', views.aumentasesion, name="aumentasesion"),
    path('planes/', views.planes, name="planes"),
    path('validaplanes/', views.validaplanes, name="validaplanes"),
    path('crearplanes/', views.crearplanes, name="crearplanes"),
    path('sesion/', views.sesion, name="sesion"),
    path('sesion2/', views.sesion2, name="sesion2"),
    path('sugerencias/', views.sugerencias, name="sugerencias"),
    path('', views.index, name="index"),
]


