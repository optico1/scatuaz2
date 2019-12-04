from django.test import TestCase
from trabajador.models import Trabajador
from trabajador.forms import TrabajadorForm
from django.core.exceptions import ValidationError


class TestModels(TestCase):

    def test_si_el_formulario_es_valido(self):
        trabajador = Trabajador.objects.create(
            nombre='Juan',
            paterno='Ramos',
            materno='Garcia',
            rfc='RAGJ7701229W3',
            curp='RAGJ770122HZSMRN04',
        )
        trabajador_uno = Trabajador.objects.first()
        self.assertEqual(trabajador, trabajador_uno)


    
    def test_si_el_formulario_es_invalido_sin_nombre(self):

        data = {
            'nombre':'',
            'paterno':'Berumen',
            'materno':'Murillo',
            'rfc':'VECJ88032XX',
            'curp':'BEMF17MZSRRT06',
        }
        
        form = TrabajadorForm(
            data
        )
        self.assertFalse(form.is_valid())


    def test_si_el_formulario_es_invalido_mas_de_100_caracteres_en_nombre(self):

        data = {
            'nombre':'Fatimaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
            'paterno':'Berumen',
            'materno':'Murillo',
            'rfc':'VECJ88032XX',
            'curp':'BEMF17MZSRRT06',
        }
        
        form = TrabajadorForm(
            data
        )
        self.assertFalse(form.is_valid())


    def test_si_el_formulario_es_invalido_mas_de_13_caracteres_en_rfc(self):

        data = {
            'nombre':'Fatima',
            'paterno':'Berumen',
            'materno':'Murillo',
            'rfc':'VECJ8sdsdsadasdasd8032XX',
            'curp':'BEMF17MZSRRT06',
        }
        
        form = TrabajadorForm(
            data
        )
        self.assertFalse(form.is_valid())