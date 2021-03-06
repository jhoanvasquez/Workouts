from django.forms import ModelForm
#from .models import Prueba
from django.contrib.auth.forms import UserCreationForm
from .models import UserModel, habilidadesUser
from django import forms

class RegistroForm(ModelForm):
    
    
    class Meta:
        model = UserModel
        fields = '__all__'

class SkillsForm(ModelForm):
    model = habilidadesUser