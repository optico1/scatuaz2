from django.test import TestCase
from django.urls import reverse

class TestView(TestCase):

    def test_url_lista_trabajadores(self):
        response = self.client.get('/trabajador/')
        self.assertEqual(response.status_code, 200)

    def test_nombre_url_lista_trabajadores(self):
        response = self.client.get(reverse('lista_trabajador'))
        self.assertEqual(response.status_code, 200)
  
    def test_template_lista_trabajadores(self):
        response = self.client.get('/trabajador/')
        self.assertTemplateUsed(response, 'lista_trabajador.html')
    
    def test_url_buscar_trabajadores(self):
        response = self.client.get('/trabajador/buscar')
        self.assertEqual(response.status_code, 200)

    def test_nombre_url_buscar_trabajadores(self):
        response = self.client.get(reverse('buscar_trabajador'))
        self.assertEqual(response.status_code, 200)
  
    def test_template_buscar_trabajadores(self):
        response = self.client.get('/trabajador/buscar')
        self.assertTemplateUsed(response, 'buscar_trabajador.html')

    def test_url_agregar_trabajadores(self):
        response = self.client.get('/trabajador/agregar')
        self.assertEqual(response.status_code, 200)

    def test_nombre_url_agregar_trabajadores(self):
        response = self.client.get(reverse('agregar_trabajador'))
        self.assertEqual(response.status_code, 200)
  
    def test_template_agregar_trabajadores(self):
        response = self.client.get('/trabajador/agregar')
        self.assertTemplateUsed(response, 'agregar_trabajador.html')

    def test_campo_buscador_existe_en_trabajadores(self):
        response = self.client.get(reverse('lista_trabajador'))
        # print(response.content)
        self.assertInHTML('id_buscador', response.content.decode("utf-8"))