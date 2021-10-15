from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import admin
from django.contrib.auth.models import User
from datetime import date
from datetime import datetime

from django.forms.widgets import DateInput
from .models import Areas, Rangos, Habilidades, Ejercicios, Sesion_Ejercicio, Sesiones, Planes, Usuarios



class DashboardForm(ModelForm):
    class Meta:
        model = Planes
        fields = ["id_plan","id_area"]



class PlanesForm(ModelForm):

    #id_plan=forms.ModelChoiceField(label="Id Plan" , queryset=)
    id_area = forms.ModelChoiceField(label="Id Area" , queryset=Areas.objects.all(), widget=forms.Select(attrs={'class': 'form-control w-50'}))
    #id_usuario= forms.ModelChoiceField(label="Id Usuario" , queryset=Usuarios.objects.get(fk_user=nameusuario))
    #id_rango = forms.ModelChoiceField(label="Id Rango" , queryset=Rangos.objects.all())
    
    #dias_disponibles = forms.IntegerField(label="Dias Disponibles" ,widget=forms.TextInput(attrs={'class': 'form-control', 'type':'number'}))
    #dias_entrenados = forms.IntegerField(label="Dias Entrenados" ,widget=forms.TextInput(attrs={'class': 'form-control', 'type':'number'}))
    #dias_esta_semana = forms.IntegerField(label="Dias esta semana" ,widget=forms.TextInput(attrs={'class': 'form-control', 'type':'number'}))
    #num_sesiones = forms.IntegerField(label="Numero de sesiones" ,widget=forms.TextInput(attrs={'class': 'form-control', 'type':'number'}))
    #ultima_semana =forms.DateField(label="Ultima Semana" , initial=datetime.now())
    
    class Meta:
        model = Planes
        #fields =('id_area','ultima_semana')
        fields = ['id_area']