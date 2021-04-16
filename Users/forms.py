from django.forms import ModelForm
#from .models import Prueba
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from WorkoutsApp.models import Usuarios, Habilidades


class RegistroForm(ModelForm):
    
    
    class Meta:
        model = Usuarios
        fields = '__all__'

class SkillsForm(ModelForm):

    class Meta:
        model = Habilidades
        fields = '__all__'