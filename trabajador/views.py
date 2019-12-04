from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import ListView
from .models import Buscar, Trabajador
from .forms import TrabajadorForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.

def buscar_trabajador(request):
    query = request.GET.get('buscador')
    trabajadores = Trabajador.objects.filter(
        Q(nombre=query) | Q(paterno=query) | Q(materno=query) | Q(rfc=query)
    )
    context = {
        'trabajadores': trabajadores,
    }
    return render(request, 'buscar_trabajador.html', context)

def lista_trabajador(request):
    trabajadores = Trabajador.objects.all()
    context = {
        'trabajadores': trabajadores,
        'llave': 'Esta llave es secreta',
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
    try:
        trabajador = Trabajador.objects.get(pk=id)
        trabajador.delete()
        return redirect('lista_trabajador')
    except Trabajador.DoesNotExist:
        trabajadores = Trabajador.objects.all()
        context = {
            'trabajadores': trabajadores,
            'llave': 'Esta llave es secreta',
        }
        return render(request, 'lista_trabajador.html', context)

def modificar_trabajador(request, id):
    pass
