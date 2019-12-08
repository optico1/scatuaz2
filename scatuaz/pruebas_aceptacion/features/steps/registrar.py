from behave import given, when, then


@given(u'que soy un administrador logeado')
def step_impl(context):
    iniciar_sesion(context)


@when(u'ingreso los datos de "{user_f}": "{user}", "{password_f}": "{password}", "{email_f}": "{email}"')
def step_impl(context, user_f, user, password_f, password, email_f, email):
    context.driver.find_element_by_id('id_'+user_f).send_keys(user)
    context.driver.find_element_by_id('id_'+password_f).send_keys(password)
    context.driver.find_element_by_id('id_'+email_f).send_keys(email)


@when(u'doy click en "Agregar"')
def step_impl(context):
    context.driver.find_elements_by_xpath("//*[contains(text(), 'Agregar')]").click()   


@then(u'puedo ver "elmickey" en la lista de usuarios')
def step_impl(context):
    pass


@when(u'selecciono la casilla de administrador')
def step_impl(context):
    pass


@then(u'puedo ver que la casilla de "admin" esta checada')
def step_impl(context):
    pass

def iniciar_sesion(context):
    context.driver.get(context.url+'')
    context.driver.find_element_by_id('id_username').send_keys('tigre')
    context.driver.find_element_by_id('id_password').send_keys('tigre123')