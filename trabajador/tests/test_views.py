from django.test import TestCase
from django.urls import reverse
from trabajador.models import Trabajador

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

    def test_campo_buscador_existe_en_trabajadores(self):
        response = self.client.get('/trabajador/')
        self.assertInHTML('<input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search" name="buscador" id="buscador">', response.content.decode("utf-8"))

    def test_url_buscar_trabajadores(self):
        response = self.client.get('/trabajador/buscar')
        self.assertEqual(response.status_code, 200)

    def test_nombre_url_buscar_trabajadores(self):
        response = self.client.get(reverse('buscar_trabajador'))
        self.assertEqual(response.status_code, 200)
  
    def test_template_buscar_trabajadores(self):
        response = self.client.get('/trabajador/buscar')
        self.assertTemplateUsed(response, 'buscar_trabajador.html')
    
    def test_resultado_busqueda_existente(self):
        Trabajador.objects.create(
            nombre='Salvador',
            paterno='Loera',
            materno='Quiroz',
            rfc='LOQSY32231',
            curp='LOQS960920HNLRRL09'
        )

        response = self.client.get('/trabajador/buscar?buscador=Salvador')
        self.assertInHTML('<td>Salvador</td>', response.content.decode("utf-8"))
        self.assertInHTML('<td>Loera</td>', response.content.decode("utf-8"))
        self.assertInHTML('<td>Quiroz</td>', response.content.decode("utf-8"))
        response = self.client.get('/trabajador/buscar?buscador=Loera')
        self.assertInHTML('<td>Salvador</td>', response.content.decode("utf-8"))
        self.assertInHTML('<td>Loera</td>', response.content.decode("utf-8"))
        self.assertInHTML('<td>Quiroz</td>', response.content.decode("utf-8"))
        response = self.client.get('/trabajador/buscar?buscador=Quiroz')
        self.assertInHTML('<td>Salvador</td>', response.content.decode("utf-8"))
        self.assertInHTML('<td>Loera</td>', response.content.decode("utf-8"))
        self.assertInHTML('<td>Quiroz</td>', response.content.decode("utf-8"))
    
    def test_no_hay_resultados(self):
        response = self.client.get('/trabajador/buscar?buscador=Elseñornoexiste')
        self.assertInHTML('<h2>No hay resultados</h2>', response.content.decode("utf-8"))
    
    def test_busqueda_vacia_regresa_cero_resultados(self):
        self.agregar_trabajador2

        response = self.client.get('/trabajador/buscar?buscador=')
        self.assertInHTML('<h2>No hay resultados</h2>', response.content.decode("utf-8"))
    
    def test_varios_resultados(self):
        self.agregar_trabajador1()
        self.agregar_trabajador2()

        response = self.client.get('/trabajador/buscar?buscador=Loera')
        self.assertInHTML('<td>Salvador</td>', response.content.decode("utf-8"))
        self.assertInHTML('<td>Loera</td>', response.content.decode("utf-8"))
        self.assertInHTML('<td>Quiroz</td>', response.content.decode("utf-8"))
        self.assertInHTML('<td>Fatima Anahi</td>', response.content.decode("utf-8"))
        self.assertInHTML('<td>Loera</td>', response.content.decode("utf-8"))
        self.assertInHTML('<td>Murillo</td>', response.content.decode("utf-8"))
    
    def test_muestra_rfc_en_resultados(self):
        self.agregar_trabajador1()

        response = self.client.get('/trabajador/buscar?buscador=Loera')
        self.assertInHTML('<td>LOQSY32231</td>', response.content.decode("utf-8"))
    
    def test_muestra_cantidad_de_resultados(self):
        self.agregar_trabajador1()
        self.agregar_trabajador2()

        response = self.client.get('/trabajador/buscar?buscador=Loera')
        self.assertInHTML('<p>2 resultados.</p>', response.content.decode("utf-8"))
    
    def agregar_trabajador1(self):
        Trabajador.objects.create(
            nombre='Salvador',
            paterno='Loera',
            materno='Quiroz',
            rfc='LOQSY32231',
            curp='LOQS960920HNLRRL09'
        )
    
    def agregar_trabajador2(self):
        Trabajador.objects.create(
            nombre='Fatima Anahi',
            paterno='Loera',
            materno='Murillo',
            rfc='BMFA27182DS',
            curp='BMFA21873HJDSA98SS'
        )