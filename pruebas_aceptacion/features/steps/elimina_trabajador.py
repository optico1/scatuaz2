@given(u'Que ingreso a la lista de los trabajadores')
def step_impl(context):
    context.driver.get('http://192.168.0.49:8000/periodo/dinos')

@given(u'encuentro al trabajador "pedro"')
def step_impl(context):
    pass

@when(u'presiono el botón eliminar')
def step_impl(context):
    pass

@when(u'confirmo la eliminación en la segunda pantalla')
def step_impl(context):
    pass

@then(u'ya no puedo ver el trabajador "pedro" en la lista de trabajadores.')
def step_impl(context):
    pass