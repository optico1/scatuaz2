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
    

    def test_url_agregar_trabajadores(self):
        response = self.client.get('/trabajador/agregar')
        self.assertEqual(response.status_code, 200)

    def test_nombre_url_agregar_trabajadores(self):
        response = self.client.get(reverse('agregar_trabajador'))
        self.assertEqual(response.status_code, 200)
  
    def test_template_agregar_trabajadores(self):
        response = self.client.get('/trabajador/agregar')
        self.assertTemplateUsed(response, 'agregar_trabajador.html')

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