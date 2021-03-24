from django.forms import ModelForm
from .models import Planes
from django import forms

from django.contrib.auth.forms import UserCreationForm


class DashboardForm(ModelForm):
    class Meta:
        model = Planes
        fields = ["id_plan","id_area"]

