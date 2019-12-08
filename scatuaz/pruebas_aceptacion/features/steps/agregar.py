from behave import given, when, then
from selenium import webdriver
from unittest import TestCase


@given(u'que ingreso al formulario para llenar los datos del trabajador')
def step_impl(context):
    context.driver.get('http://192.168.33.10:8080/trabajador/agregar')


@given(u'escribo los datos: "{nombre}", "{paterno}", "{materno}", "{rfc}", "{curp}"')
def step_impl(context, nombre, paterno, materno, rfc, curp):
    context.driver.find_element_by_id('id_nombre').send_keys(nombre)
    context.driver.find_element_by_id('id_paterno').send_keys(paterno)
    context.driver.find_element_by_id('id_materno').send_keys(materno)
    context.driver.find_element_by_id('id_rfc').send_keys(rfc)
    context.driver.find_element_by_id('id_curp').send_keys(curp)


@when(u'de clic en el botón crear trabajador')
def step_impl(context):
    context.driver.find_element_by_class_name('btn-primary').click()


@then(u'podré ver el trabajador "{trabajador}" en la lista de trabajador')
def step_impl(context,trabajador):
    rows = context.driver.find_elements_by_tag_name('tr')
    trabajadores = [row.find_elements_by_tag_name('td')[1].text for row in rows[1:]]
    
    context.test.assertIn(trabajador, trabajadores)



@then(u'no podré ver el trabajador "{trabajador}" en la lista de trabajador')
def step_impl(context,trabajador):
    context.driver.get('http://192.168.33.10:8080/trabajador')
    rows = context.driver.find_elements_by_tag_name('tr')
    trabajadores = [row.find_elements_by_tag_name('td')[1].text for row in rows[1:]]
    
    context.test.assertNotIn(trabajador, trabajadores)

@then(u'podré ver el mensaje de "{mensaje}"')
def step_impl(context, mensaje):
    lis = context.driver.find_elements_by_tag_name('li')
    errores = [li.text for li in lis]

    context.test.assertIn(mensaje, errores)