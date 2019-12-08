from django.test import TestCase
from django.core.exceptions import ValidationError


class Test_View_eliminar(TestCase):
    
    def test_url_trabajadores_eliminar(self):
        response = self.client.get('/trabajador/eliminar')
        self.assertEqual(response.status_code, 200)    
 
    def test_template_trabajador_eliminar(self):
        response = self.client.get('/trabajador/eliminar')
        self.assertTemplateUsed(response, 'confirm_delete.html')        