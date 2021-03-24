from django.shortcuts import render
from django.http import HttpResponse
from .forms import DashboardForm
from .models import Usuarios
from .models import Planes
from .models import Areas
""" from models import *  """

# Create your views here.

def register(request):
    return render(request, 'WorkoutsApp/register.html')

    
def dashboard(request):
    

    formulario=DashboardForm()
    usuarios = Usuarios.objects.all()
    areas = Areas.objects.all()
    planentreno = Planes.objects.all()
    context = {
       "nombre": request.user,
        "apellido": "Abreu",
        'form': formulario,
        "usuarios": usuarios,
        "areas": areas,
        "planentreno": planentreno
    }

    return render(request, 'dashboard.html', context )