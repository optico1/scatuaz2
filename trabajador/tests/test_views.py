from django.test import TestCase

class TestView(TestCase):

    def test_url_buscar_trabajadores(self):
        response = self.client.get('trabajador/buscar')
        self.assertEqual(response.status_code, 200)