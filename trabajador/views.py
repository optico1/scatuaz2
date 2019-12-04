from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Buscar, Trabajador
from .forms import TrabajadorForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.
#class ListaDino(PermissionRequiredMixin, ListView):
class ListaTrabajador(ListView):
    template_name = 'lista_trabajador.html'
    model = Trabajador

class BuscarTrabajador(ListView):
    template_name = 'buscar_trabajador.html'
    model = Buscar

def buscar_trabajador(request):
    return render(request, 'buscar_trabajador.html', {})

def lista_trabajador(request):
    trabajadores = Trabajador.objects.all()
    context = {
        'trabajadores': trabajadores,
    }

    return render(request, 'lista_trabajador.html', context)

def agregar_trabajador(request):
    if request.method == 'POST':
        form = TrabajadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_trabajador')
    else:
        form = TrabajadorForm()
    return render(request, 'agregar_trabajador.html', {'form':form})

def eliminar_trabajador(request, id):
    pass

def modificar_trabajador(request, id):
    pass