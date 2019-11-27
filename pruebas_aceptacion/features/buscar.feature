Característica: Buscar un trabajador
    Como usuario del sistema SCATUAZ, quiero buscar trabajadores a partir de valores dados.

    Escenario: Buscar un trabajador con nombre Jaime
        Dado que ingreso a la vista de "trabajador"
        Y ingreso el nombre de "Juan" en el buscador
        Cuando doy clic en "buscar"
        Entonces puedo ver "Juan Pérez Marila", "Jaime Manuel Sanchez Gutierrez", "Jaime Torres Vela" en la lista de resultados

    # Escenario: Buscar un trabajador con nombre Jaim
    #     Dado que ingreso el nombre Jaim
    #     Cuando se realiza una busqueda
    #     Entonces puedo ver No hay resultados
    
    # Escenario: Buscar un trabajador con rfc LOQS980920HNLRRL09
    #     Dado que ingreso el rfc LOQS980920HNLRRL09
    #     Cuando se realiza una busqueda
    #     Entonces puedo ver Salvador Loera Quiroz
    
    # Escenario: Buscar un trabajador con rfc LOQS98
    #     Dado que ingreso el rfc LOQS98
    #     Cuando se realiza una busqueda
    #     Entonces puedo ver No hay resultados
    
    # Escenario: Buscar un trabajador con
    #     Dado que ingreso el
    #     Cuando se realiza una busqueda
    #     Entonces puedo ver Campo de busqueda vacion