from django.test import TestCase
from trabajador.models import Trabajador
from django.core.exceptions import ValidationError
import unittest

class TestModels(unittest.TestCase):
    def test_return_object_trabajador(self):
        trabajador = Trabajador(
            nombre='Juan',
            paterno='Ramos',
            materno='Garcia',
            rfc='RAGJ7701229W3',
            curp='RAGJ770122HZSMRN04',
        )
        trabajador.save()
        self.assertEqual(trabajador.nombre, trabajador.__str__())
    

    def test_max_length_en_nombre(self):

        trabajador = Trabajador(
            nombre='Juan',
            paterno='Ramos',
            materno='Garcia',
            rfc='RAGJ7701229W3',
            curp='RAGJ770122HZSMRN04',
        )
        
        
        self.assertLess(len(trabajador.nombre),100)

    def test_mas_de_la_max_length_en_nombre(self):

        trabajador = Trabajador(
            nombre='Juaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaan',
            paterno='Ramos',
            materno='Garcia',
            rfc='RAGJ7701229W3',
            curp='RAGJ770122HZSMRN04',
        )
        
        
        self.assertGreater(len(trabajador.nombre),100)

    def test_insercion_del_trabajador(self):
        trabajador = Trabajador(
            nombre='Juan',
            paterno='Ramos',
            materno='Garcia',
            rfc='RAGJ7901629W3',
            curp='RAGJ770522HZSMRN04',
        )
        trabajador.save()

        self.assertEqual(Trabajador.objects.all()[0], trabajador)

    def test_no_insercion_del_trabajador_repetido(self):
        trabajador = Trabajador(
            nombre='Juan',
            paterno='Ramos',
            materno='Garcia',
            rfc='REGJ7901629W3',
            curp='REGJ770522HZSMRN04',
        )
        trabajador.save()

        self.assertNotEqual(Trabajador.objects.all()[0], trabajador)
