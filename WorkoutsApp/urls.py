
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('registerskills/', views.registerSkills, name="register2"),
    path('login/', views.login, name="login")
]