from django.test import TestCase
from django.core.exceptions import ValidationError
from login.forms import UserForm
from login.models import Usuario,User

class Test_View_Usuario(TestCase):
    def test_status_nuevo_usuario(self):
        response = self.client.get('/login/registro');
        self.assertEquals(response.status_code,200)

    def test_status_ingresar(self):
        response = self.client.get('/login/ingresar');
        self.assertEquals(response.status_code,200)

    def test_status_home(self):
        response = self.client.get('/login/home');
        self.assertEquals(response.status_code,200)

    def test_template_nuevo_usuario(self):
        response = self.client.get('/login/registro');
        self.assertTemplateUsed(response,'login/registro.html')

    def test_template_ingresar(self):
        response = self.client.get('/login/ingresar');
        self.assertTemplateUsed(response,'login/iniciar.html')

    def test_template_base_cualquier_url(self):
        response = self.client.get('/login/ingresar');
        self.assertTemplateUsed(response,'base.html')