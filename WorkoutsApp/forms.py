from django.forms import ModelForm
from .models import Planes
from django import forms

class DashboardForm(ModelForm):
    class Meta:
        model = Planes
        fields = ["id_plan","id_area"]