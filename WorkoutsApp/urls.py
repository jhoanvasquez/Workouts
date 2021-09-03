from django.contrib import admin
from django.urls import path

from WorkoutsApp import views
from . import views


urlpatterns = [

    #path('admin/', admin.site.urls), 
    path('register/', views.register, name="register"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('planes/', views.planes, name="planes"),
    path('sesion/', views.sesion, name="sesion"),
    path('sugerencias/', views.sugerencias, name="sugerencias"),
    path('', views.index, name="index"),
]


