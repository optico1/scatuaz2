from django.test import TestCase
from django.core.exceptions import ValidationError
from login.forms import UserForm,UsuarioForm
from login.models import Usuario,User

class Test_Form_User(TestCase):
    def test_form_valid_user(self):
        dataUsuario ={
            'username' : 'tigrito',
            'password': 'tigrito123',
            'password_re' : 'tigrito123'
        }
        form = UserForm(
            dataUsuario
        )
        self.assertTrue(form.is_valid())

    def test_form_invalid_user(self):
        dataUsuario ={
            'username' : 'tigrito',
            'password': 'tigrito123',
            'password_re' : 'tigrito1234'
        }
        form = UserForm(
            dataUsuario
        )
        self.assertFalse(form.is_valid())

    def test_form_data_personal_valid(self):
        """
        dataUsuario ={
            'username' : 'desconocido',
            'password': 'tigrito123',
            'password_re' : 'tigrito123'
        }
        """
        dataPersonal ={
            'nombre' : 'eduardo',
            'correo' : 'lalo@gmail.com'
        }
        form = UsuarioForm(
            dataPersonal
        )
        """
        form = UserForm(
            dataUsuario
        )
        """
        self.assertTrue(form.is_valid())

    def test_form_data_personal_invalid(self):
        dataPersonal ={
            'nombre' : '',
            'correo' : 'lalo@gmail.com'
        }
        form = UsuarioForm(
            dataPersonal
        )
        self.assertFalse(form.is_valid())



    