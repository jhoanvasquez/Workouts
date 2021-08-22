from django.contrib import admin
from django.urls import path

from WorkoutsApp import views
from . import views


urlpatterns = [

    #path('admin/', admin.site.urls), 
    path('register/', views.register, name="register"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('sugerencias/', views.sugerencias, name="sugerencias"),
    path('sesion/', views.sesion, name="sesion"),
    path('', views.index, name="index"),
]


