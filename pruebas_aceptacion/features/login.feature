Característica: Inicio de sesión de un usuario
    Como usuario del sistema SCATUAZ, 
    Quiero iniciar sesion haciendo uso de mis credenciales
    Para acceder a las funciones del sistema

    Escenario: Iniciar sesion con usuario tigrito y con contraseña tigre123
        Dado que ingreso el usuario "tigrito" y la contraseña "tigre123"
        Cuando se realiza un inicio de sesion
        Entonces puedo ver una bandera de "Bienvenido"
    
    Escenario: Iniciar sesion erroneamente con usuario tigrito y con contraseña ti542234
        Dado que ingreso el usuario "tigrito" con la contraseña "ti542234"
        Cuando se realiza un inicio de sesion
        Entonces puedo ver una bandera de "error"
    
    Escenario: Iniciar sesion sin usuario y contraseña 
        Dado que no ingreso el usuario ni la contraseña
        Cuando se realiza un inicio de sesion
        Entonces me mantengo en la misma pagina
