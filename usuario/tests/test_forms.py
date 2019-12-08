from django.test import TestCase
from trabajador.forms import TrabajadorForm


class TestFormModificarUsuario(TestCase):
    
    #43 name
    

    def test_si_el_formulario_es_invalido_mas_de_43_caracteres_en_username(self):

        data = {
            'username':'tigritooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo',
            'email':'tigre@hotmail.com',
        }
        
        form = TrabajadorForm(
            data
        )
        self.assertFalse(form.is_valid())
        
    def test_si_el_formulario_es_invalido_sin_nombre(self):
        pass
    