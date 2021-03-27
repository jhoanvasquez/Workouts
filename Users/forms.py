from django.forms import ModelForm
#from .models import Prueba
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserModel, habilidadesUser


class RegistroForm(ModelForm):
    
    
    class Meta:
        model = UserModel
        fields = '__all__'

class SkillsForm(ModelForm):

    class Meta:
        model = habilidadesUser
        fields = '__all__'