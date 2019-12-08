from behave import given, when, then
from django.contrib.auth.models import User
from django.test import TestCase
import time

#1
@given(u'que ingreso el usuario "tigre" y la contraseña "tigre123"')
def step_impl(context):
    crear(context,)
    login(context,'tigre','tigre123')
    
@when(u'se realiza un inicio de sesion')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div/form/button').click()

@then(u'puedo ver una bandera de "Bienvenido"')
def step_impl(context):
    mensaje = context.driver.find_element_by_tag_name('h1')#driver.find_element_by_xpath('/html/body/h1')
    context.test.assertEqual(mensaje.text,"Bienvenido")

#2
@given(u'que ingreso el usuario "tigre" con la contraseña "ti542234"')
def step_impl(context):
    time.sleep(2)
    login(context,'tigre','ti542234')

@then(u'puedo ver una bandera de "error"')
def step_impl(context):
    mensaje = context.driver.find_element_by_xpath('/html/body/div/form/ul/li')
    context.test.assertEqual(mensaje.text,"Please enter a correct username and password. Note that both fields may be case-sensitive.")

#3
@given(u'que no ingreso el usuario ni la contraseña')
def step_impl(context):
    time.sleep(2)
    context.driver.get(context.url+'')
    context.driver.find_element_by_xpath('/html/body/div/form/button').click()

@then(u'me mantengo en la misma pagina')
def step_impl(context):
    context.test.assertEqual(str(context.url),"http://localhost:8000/")


#login
def login(context,usr,pas):
    context.driver.get(context.url+'')
    context.driver.find_element_by_id('id_username').send_keys(usr)
    context.driver.find_element_by_id('id_password').send_keys(pas)

def crear(context,usr,pas):
    context.usuario = User.objects.create({'username': usr, 'password': pas})