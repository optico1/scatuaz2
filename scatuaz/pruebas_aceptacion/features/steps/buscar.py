from behave import given, when, then

@given(u'que ingreso a la vista de "{vista}"')
def step_impl(context, vista):
    context.driver.get(context.url+vista)

@given(u'ingreso "{llave}" en el {id_campo}')
def step_impl(context, llave, id_campo):
    context.driver.find_element_by_id(id_campo).send_keys(llave)

@when(u'doy clic en "{boton}"')
def step_impl(context, boton):
    context.driver.find_element_by_id(boton).click()

@then(u'puedo ver "{nombre}" en la vista de resultados')
def step_impl(context, nombre):
    rows = context.driver.find_elements_by_tag_name('tr')
    trabajadores = [row.find_elements_by_tag_name('td')[3].text for row in rows[1:] ]

    context.test.assertIn(nombre, trabajadores)

@then(u'puedo ver "{mensaje}"')
def step_impl(context, mensaje):
    h2s = context.driver.find_elements_by_tag_name('h2')
    h2stext = [h2.text for h2 in h2s]

    context.test.assertIn(mensaje, h2stext)
