from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UsuarioForm, CambiarContrasenaForm, ModificarUsuarioForm
from django.contrib.auth import login, authenticate

# Create your views here.

@login_required
def lista_usuario(request):
    if request.user.is_superuser:
        usuarios = User.objects.all()
        context = {
            'usuarios': usuarios,
        }
        return render(request, 'lista_usuario.html', context)
    return redirect('lista_trabajador')


@login_required
def agregar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuario')
    else:
        form = UsuarioForm()
    return render(request, 'agregar_usuario.html', {'form':form})

@login_required
def eliminar_usuario(request, id):
    if request.method == 'POST':
        usuario = User.objects.get(pk=id)
        usuario.delete()
        return redirect('lista_usuario')
    else:
        usuario = User.objects.get(pk=id)
        return render(request, 'confirm_delete_user.html', {'usuario': usuario})

@login_required
def modificar_usuario(request, id):
    usuario = User.objects.get(pk=id)
    if request.method == 'POST':
        form = ModificarUsuarioForm(request.POST, instance=usuario) 
        if form.is_valid():
            form.save()
            return redirect('lista_usuario')
    else:
        form = ModificarUsuarioForm(instance=usuario)
    return render(request, 'modificar_usuario.html', {'form':form, 'usuario':usuario})

@login_required
def cambiar_contrasena(request, id):
    usuario = User.objects.get(pk=id)
    if request.method == 'POST':
        form = CambiarContrasenaForm(usuario, data=request.POST) 
        if form.is_valid():
            form.clean_new_password2()
            form.save()
            return redirect('lista_usuario')
    else:
        form = CambiarContrasenaForm(usuario)
    return render(request, 'cambiar_contrasena.html', {'form':form, 'usuario':usuario})