from django.shortcuts import render
from .models import Trabajador
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

class ListaTrabajador(ListView):
    model = Trabajador
    template_name = 'ListaTrabajador.html'
    
class eliminar_trabajador(DeleteView):
    model = Trabajador
    success_url = reverse_lazy('ListaTrabajador.html')
    template_name = 'confirm_delete.html'



