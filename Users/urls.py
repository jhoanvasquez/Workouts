from django.contrib.auth.views import logout_then_login
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('registerskills/', views.registerSkills, name="register2"),
    path('accounts/login/', views.login, name="login"),
    path('logout/', logout_then_login, name="logout"),
    path('perfil/', views.perfil, name="perfil"),
    
]