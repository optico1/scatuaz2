from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Trabajador, Actualizacion
from .forms import TrabajadorForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def buscar_trabajador(request):
    query = request.GET.get('buscador')
    trabajadores = Trabajador.objects.filter(
        Q(nombre=query) | Q(paterno=query) | Q(materno=query) | Q(rfc=query)
    )
    context = {
        'trabajadores': trabajadores,
    }
    return render(request, 'buscar_trabajador.html', context)

@login_required
def lista_trabajador(request):
    trabajadores = Trabajador.objects.all()
    context = {
        'trabajadores': trabajadores,
        'llave': 'Esta llave es secreta',
    }

    return render(request, 'lista_trabajador.html', context)

@login_required
def ver_trabajador(request, id):
    trabajador = Trabajador.objects.get(pk=id)
    usuario = User.objects.get(pk=trabajador.alta_usuario)
    try:
        actualizaciones = Actualizacion.objects.filter(id_trabajador=id)
    except:
        actualizaciones = ()
    context = {
        'trabajador': trabajador,
        'usuario': usuario,
        'actualizaciones': actualizaciones
    }

    return render(request, 'ver_trabajador.html', context)

@login_required
def agregar_trabajador(request):
    if request.method == 'POST':
        form = TrabajadorForm(request.POST)
        if form.is_valid():
            tmp = form.save(commit=False)
            tmp.alta_usuario = request.user.id
            tmp.save()
            return redirect('lista_trabajador')
    else:
        form = TrabajadorForm()
    return render(request, 'agregar_trabajador.html', {'form':form})

@login_required
def eliminar_trabajador(request, pk):
    if request.method == 'POST':
        try:
            trabajador = Trabajador.objects.get(pk=pk)
            trabajador.delete()
            return redirect('lista_trabajador')
        except Trabajador.DoesNotExist:
            trabajadores = Trabajador.objects.all()
            context = {
                'trabajadores': trabajadores
            }
            return render(request, 'lista_trabajador.html', context)
    else:
        trabajador = Trabajador.objects.get(pk=pk)
        return render(request, 'confirm_delete.html', {'trabajador': trabajador})

@login_required
def modificar_trabajador(request, id):
    trabajador = Trabajador.objects.get(pk=id)
    if request.method == 'POST':
        form = TrabajadorForm(request.POST, instance=trabajador) 
        if form.is_valid():
            form.save()
            Actualizacion.objects.create(id_trabajador=trabajador, usuario=request.user.username)
            return redirect('lista_trabajador')
    else:
        form = TrabajadorForm(instance=trabajador)
    return render(request, 'modificar_trabajador.html', {'form':form})
