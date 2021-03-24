from django.contrib.auth.views import logout_then_login
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('registerskills/', views.registerSkills, name="register2"),
    path('accounts/login/', views.login, name="login"),
    path('logout/', logout_then_login, name="logout"),
    path('perfil/', views.perfil, name="perfil"),
    path('update/', views.update, name="editarPerfil"),
    path('changePassword/', views.cambiarContra, name="cambiarContra"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]