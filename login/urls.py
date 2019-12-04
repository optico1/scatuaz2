from django.urls import path
from . import views

urlpatterns = [
    path('registro', views.NuevoUsuario.as_view(), name='nuevo_usuario'),
    path('ingresar', views.Login.as_view(), name='ingresar'),
    path('home', views.Home.as_view(), name='home'),

]
