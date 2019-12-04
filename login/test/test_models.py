from django.test import TestCase
from django.core.exceptions import ValidationError
from login.forms import UserForm
from login.models import Usuario, User
from django.db.utils import IntegrityError

class Test_Model_User(TestCase):

    def test_count_user(self):
        User.objects.create_user(
            username="desconocido",
            email="desconocido@gmail.com",
            password="desconocido123"
        )
        self.assertEqual(User.objects.count(), 1)
    
    def test_name_user(self):
        user = User.objects.create_user(
            username="desconocido",
            email="desconocido@gmail.com",
            password="desconocido123"
        )
        """
        Usuario.objects.create(
            nombre = 'lalo',
            correo= 'lalito@gmail.com',
        )
        """
        #print("HAY:")
        #print(User.objects.count())
        #print(Usuario.objects.count())
        self.assertEqual(user.__str__(), 'desconocido')
    
    def test_user_name_max(self):
        try:
            User.objects.create_user(
            username="desconocido1",
            email="desconocido@gmail.com",
            password="desconocido123"
            )
            User.objects.create_user(
            username="desconocido1",
            email="desconocido@gmail.com",
            password="desconocido123"
            )
        except IntegrityError as ex:
            self.assertEqual(''+str(ex)+'',"UNIQUE constraint failed: auth_user.username")
        