from django.test import TestCase
from trabajador.forms import TrabajadorForm


class TestFormModificarUsuario(TestCase):
    
    def test_si_el_formulario_es_invalido_mas_de_43_caracteres_en_username(self):

        data = {
            'username':'tigritooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo',
            'email':'tigre@hotmail.com',
        }
        
        form = TrabajadorForm(
            data
        )
        self.assertFalse(form.is_valid())
        
    def test_si_el_formulario_es_invalido_sin_username(self):
        data = {
            'username':'',
            'email':'tigre@hotmail.com',
        }
        
        form = TrabajadorForm(
            data
        )
        self.assertFalse(form.is_valid())
        
    def test_si_el_email_es_incorrecto_incompleto(self):
        data = {
            'username':'tigrito',
            'email':'tigre@',
        }
        
        form = TrabajadorForm(
            data
        )
        self.assertFalse(form.is_valid()) 
        
        
    def test_si_el_email_es_incorrecto(self):
        data = {
            'username':'tigrito',
            'email':'tigre@hot',
        }
        
        form = TrabajadorForm(
            data
        )
        self.assertFalse(form.is_valid()) 
        
    
    def test_si_el_formulario_es_invalido_sin_email(self):
        data = {
            'username':'tigrito',
            'email':'',
        }
        
        form = TrabajadorForm(
            data
        )
        self.assertFalse(form.is_valid())