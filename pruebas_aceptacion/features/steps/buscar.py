from behave import given, when, then

@given(u'que ingreso a la vista de "trabajador"')
def step_impl(context):
    context.driver.get(context.url+'trabajador')

@given(u'ingreso el nombre de "Juan" en el buscador')
def step_impl(context):
    context.driver.find_element_by_id('id_campo_buscador').send_keys('Juan')
    pass

@when(u'doy clic en "buscar"')
def step_impl(context):
    pass

@then(u'puedo ver "{res1}", "{res2}", "{res3}" en la vista de resultados')
def step_impl(context, res1, res2, res3):
    pass