from django.test import TestCase
from usuario.forms import ModificarUsuarioForm, UsuarioForm 


class TestFormModificarUsuario(TestCase):

    def test_si_el_formulario_es_invalido_mas_de_43_caracteres_en_username(self):

        data = {
            'username':'tigritooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo',
            'email':'tigre@hotmail.com',
        }
        
        form = UsuarioForm(
            data
        )
        self.assertFalse(form.is_valid())
        
    def test_si_el_formulario_es_invalido_sin_username(self):
        data = {
            'username':'',
            'email':'tigre@hotmail.com',
        }
        
        form = UsuarioForm(
            data
        )
        self.assertFalse(form.is_valid())
        
    def test_si_el_email_es_incorrecto_incompleto(self):
        data = {
            'username':'tigrito',
            'email':'tigre@',
        }
        
        form = UsuarioForm(
            data
        )
        self.assertFalse(form.is_valid()) 
        
        
    def test_si_el_email_es_incorrecto(self):
        data = {
            'username':'tigrito',
            'email':'tigre@hot',
        }
        
        form = UsuarioForm(
            data
        )
        self.assertFalse(form.is_valid()) 
        
    
    def test_si_el_formulario_es_invalido_sin_email(self):
        data = {
            'username':'tigrito',
            'email':'',
        }
        
        form = UsuarioForm(
            data
        )
        self.assertFalse(form.is_valid())
        
    def test_si_el_formulario_es_invalido_sin_nueva_contraseña(self):
        data = {
            'password1':'',
            'password2':'tigrito123',
        }
        
        form = UsuarioForm(
            data
        )
        self.assertFalse(form.is_valid())
        
    def test_si_el_formulario_es_invalido_sin_Repita_Nueva_contraseña(self):
        data = {
            'password1':'tigrito123',
            'password2':'',
        }
        
        form = UsuarioForm(
            data
        )
        self.assertFalse(form.is_valid())
        
    def test_si_el_formulario_es_invalido_no_coinciden_contraseñas(self):
        data = {
            'password1':'tigrito123',
            'password2':'admin123',
        }
        
        form = UsuarioForm(
            data
        )
        self.assertFalse(form.is_valid())