from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Usuario
from django.contrib.auth.models import User
from .forms import UsuarioForm,UserForm,LoginForm,HomeForm
from django.urls import  reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class NuevoUsuario(CreateView):
    model = User
    form_class = UserForm
    extra_context = {'usuario_form' : UsuarioForm()}
    template_name = 'login/registro.html'
    
    def form_valid(self,form):
        form_usuario = UsuarioForm(self.request.POST)#,self.request.FILES
        if form_usuario.is_valid:
            user = form.save()#commit = False)
            user.save()
            usuario = form_usuario.save()#commit = false)
            usuario = user
            usuario.save()
        else:
            return self.render_to_response(self.get_context_data(form = form, extra_context = form_usuario))
        self.object = form.save()
        return super().form_valid(form)
    
    """
    def form_invalid(self,form):
        form_usuario = UsuarioForm(self.request.POST)#,self.request.FILES
        return self.render_to_response(self.get_context_data(form = form, extra_context = form_usuario))
    """
    """
    def get_context_data(self,**kwargs):
        if 'extra_context' in kwargs:
            form_usuario = kwargs['extra']
            self.extra_context = {'form_usuario' : kwargs['form_usuario']}
        return super().get_context_data(**kwargs)
    """ 
class Login(LoginView):
    template_name = 'login/iniciar.html'
    form_class = LoginForm
    
class Home(CreateView):
    model = User
    form_class = UserForm
    extra_context = {'usuario_form' : UsuarioForm()}
    template_name = 'login/home.html'
    