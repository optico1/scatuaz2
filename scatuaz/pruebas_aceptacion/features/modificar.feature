Característica: Modificar la información de un trabajador
    Como administrador, quiero modificar la información de un trabajador para mantener actualizada su información.

    Escenario: Guardar la información modificada con el nombre faltante :
        Dado que el usuario está modificando la información del nombre " "
        Cuando presiona el botón de guardar cambios
        Entonces verá un mensaje de datos incompletos

    Escenario: Guardar la información modificada con los campos requeridos correctos :
        Dado que el usuario está modificando la información Javier Varela Sosa, VASFJ
        Cuando presiona el botón de guardar cambios
        Entonces verá un mensaje de datos guardados

    Escenario: Guarda la informaicón modificada con los campos requeridos incorrectos :
        Dado que el usuario está modificando la información 
        Y viola los criterios de entrada
        Cuando presione el botón de guardar cambios 
        Entonces verá un mensaje de error