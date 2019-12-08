from django.test import TestCase
from django.urls import reverse
from trabajador.models import Trabajador
from login.models import User
from django.contrib.auth import login

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


    def test_agrega_trabajador_form(self):
        data = {
            'nombre':'Fatima',
            'paterno':'Berumen',
            'materno':'Murillo',
            'rfc':'VECJ88032XXhh',
            'curp':'BEMF17MZSRRT06',
        }
        self.client.post('/trabajador/agregar', data=data)
        self.assertEqual(Trabajador.objects.count(), 1)

    def test_no_agregar_trabajador_repetido_form(self):
        trabajador = Trabajador(
            nombre='Fatima',
            paterno='Berumen',
            materno='Murillo',
            rfc='VECJ88032XX',
            curp='BEMF17MZSRRT06',
        )
        trabajador.save()
        data = {
            'nombre':'Fatima',
            'paterno':'Berumen',
            'materno':'Murillo',
            'rfc':'VECJ88032XX',
            'curp':'BEMF17MZSRRT06',
        }
        self.client.post('/trabajador/agregar', data=data)
        self.assertNotEqual(Trabajador.objects.count(), 2)

    def test_no_agregar_trabajador_con_curp_de_mas_de_18_caracteres_form(self):
        
        data = {
            'nombre':'Fatima',
            'paterno':'Berumen',
            'materno':'Murillo',
            'rfc':'VECJ88032XX',
            'curp':'BEMF17fdfdgdfgdfgdfgdggfgMZSRRT06',
        }
        self.client.post('/trabajador/agregar', data=data)
        self.assertEqual(Trabajador.objects.count(),0)

    def test_no_agregar_trabajador_con_rfc_de_mas_de_13_caracteres_form(self):
        
        data = {
            'nombre':'Fatima',
            'paterno':'Berumen',
            'materno':'Murillo',
            'rfc':'VECsfsdfdfsdfsdfsdfsdfsdfsdfsdfsdfJ88032XX',
            'curp':'BEMF17MZSRRT06',
        }
        self.client.post('/trabajador/agregar', data=data)
        self.assertEqual(Trabajador.objects.count(),0)

    def test_no_agregar_trabajador_si_no_tiene_nombre_form(self):
        
        data = {
            'nombre':'',
            'paterno':'Berumen',
            'materno':'Murillo',
            'rfc':'VECJ88032XX',
            'curp':'BEMF17MZSRRT06',
        }
        self.client.post('/trabajador/agregar', data=data)
        self.assertEqual(Trabajador.objects.count(),0)

    def test_no_agregar_trabajador_si_no_tiene_apellido_paterno_form(self):
        
        data = {
            'nombre':'Shavacano',
            'paterno':'',
            'materno':'Murillo',
            'rfc':'VECJ88032XX',
            'curp':'BEMF17MZSRRT06',
        }
        self.client.post('/trabajador/agregar', data=data)
        self.assertEqual(Trabajador.objects.count(),0)


    def test_no_agregar_trabajador_si_no_tiene_apellido_materno_form(self):
        
        data = {
            'nombre':'Shavacano',
            'paterno':'Loera',
            'materno':'',
            'rfc':'VECJ88032XX',
            'curp':'BEMF17MZSRRT06',
        }
        self.client.post('/trabajador/agregar', data=data)
        self.assertEqual(Trabajador.objects.count(),0)

    def test_no_agregar_trabajador_si_no_tiene_rfc_form(self):
        
        data = {
            'nombre':'Shavacano',
            'paterno':'Loera',
            'materno':'Ya No Loera',
            'rfc':'',
            'curp':'BEMF17MZSRRT06',
        }
        self.client.post('/trabajador/agregar', data=data)
        self.assertEqual(Trabajador.objects.count(),0)

    def test_no_agregar_trabajador_si_no_tiene_curp_form(self):
        
        data = {
            'nombre':'Shavacano',
            'paterno':'Loera',
            'materno':'Ya No Loera',
            'rfc':'VECJ88032XX',
            'curp':'',
        }
        self.client.post('/trabajador/agregar', data=data)
        self.assertEqual(Trabajador.objects.count(),0)

    def test_mensaje_cuando_no_hay_trabajadores(self):
        self.iniciar_sesion()

        response = self.client.get('/trabajador')
        self.assertInHTML('<h4>No hay registros.</h4>', response.content.decode("utf-8"))

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

    def iniciar_sesion(self):
        usuario = User.objects.create_user('tigrito', 'tigre@gmail.com', 'tigre123')
        login(username='tigrito', password='tigre123')