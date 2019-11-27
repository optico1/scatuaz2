from django.test import TestCase
from trabajador.models import Trabajador
from django.core.exceptions import ValidationError


# class TestModels(TestCase):

#     def test_agrega_trabajador(self):
#         trabajador = Trabajador.objects.create(
#             nombre='Juan',
#             paterno='Ramos',
#             materno='Garcia',
#             rfc='RAGJ7701229W3',
#             curp='RAGJ770122HZSMRN04',
#             sexo='Masculino',
#             estado_civil='Casado',
#             status='Activo',
#             fecha_nacimiento='22/01/1977',
#             pais_nacimiento='Mexico',
#             estado_nacimiento='32',
#             municipio_nacimiento='56',
#             lugar_nacimiento='Hospital San Miguel',
#             pais_residencia='Mexico',
#             estado_residencia='32',
#             municipio_residencia='56',
#             localidad_reside='Zacatecas',
#             calle='Paseo San Carlos 130',
#             colonia='Fraccionamiento San Fernando',
#             cp='98057',
#             telefono='1564145',
#             email='johndan@hotmail.com',
#         )
#         trabajador_uno = Trabajador.objects.first()

#         self.assertEqual(trabajador, trabajador_uno)