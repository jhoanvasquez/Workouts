from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from WorkoutsApp.models import Usuarios, Habilidades


class UserForm(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password')

class RegistroForm(ModelForm):
    
    class Meta:
        model = Usuarios
        fields = '__all__'

class SkillsForm(ModelForm):

    class Meta:
        model = Habilidades
        fields = '__all__'