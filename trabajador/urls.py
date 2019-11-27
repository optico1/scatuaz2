from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListaTrabajador.as_view(), name='lista_trabajador'),
    path('eliminar/<int:pk>',views.eliminar_trabajador.as_view(), name='eliminar_trabajador'),
    
]
