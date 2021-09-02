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
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'password'}))

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password')

class RegistroForm(forms.Form):
    edad = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'number'}))
    peso = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'type':'number', 'step':'0.01'}))
    estatura = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'type':'number', 'step':'0.01'}))
    ciudad = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Usuarios
        fields = ('edad', 'peso', 'estatura', 'ciudad')

class SkillsForm(ModelForm):

    class Meta:
        model = Habilidades
        fields = ("resistencia", "fuerza", "velocidad", "aceleracion", "agilidad", "flexibilidad", "coordinacion", "precision")

class UserFormUpdate(forms.ModelForm):

    #username = forms.CharField(label="Nombre de usuario" ,disabled= True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label="Nombre" ,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Apellido" ,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    #password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'password'}))
    

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class RegistroFormUpdate(forms.Form):
    edad = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'number'}))
    peso = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'type':'number', 'step':'0.01'}))
    estatura = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'type':'number', 'step':'0.01'}))
    ciudad = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Usuarios
        fields = ('edad', 'peso', 'estatura', 'ciudad')