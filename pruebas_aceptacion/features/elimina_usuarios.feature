Característica: Eliminar la Informacion de un Trabajador
    Como usuario del sistema SCATUAZ, quiero consultar a un trabajador a partir de valores dados y eliminarlo.

    Escenario : Consultar la informacion de un trabajador con nombre pedro y eliminarlo
        Dado que ingreso el nombre Jaime
        Cuando se realiza una busqueda
        Entonces puedo ver la información de pedro y podre eliminarlo

    Escenario: Buscar un trabajador con nombre Jaim
        Dado que ingreso el nombre Jaim
        Cuando se realiza una busqueda
        Entonces puedo ver No hay resultados y por lo tanto no se puede eliminar
    
    Escenario: Consultar la informacion de un trabajador con rfc vamj690308ghrsdasjs
        Dado que ingreso el rfc vamj690308ghrsdasjs
        Cuando se realiza una busqueda
        Entonces puedo ver la información de vamj690308ghrsdasjs y podre eliminarlo
        
    Escenario: Buscar un trabajador con rfc LOQS98
        Dado que ingreso el rfc LOQS98
        Cuando se realiza una busqueda
        Entonces puedo ver No hay resultados y por lo tanto no se puede eliminar
    
    Escenario: Buscar un trabajador con
        Dado que ingreso el
        Cuando se realiza una busqueda
        Entonces puedo ver Campo de busqueda vacio y por lo tanto no se puede eliminar