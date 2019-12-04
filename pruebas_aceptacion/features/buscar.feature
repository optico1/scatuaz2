Característica: Buscar un trabajador
    Como usuario del sistema SCATUAZ, quiero buscar trabajadores a partir de valores dados.

    Escenario: Buscar un trabajador con nombre Jaime
        Dado que ingreso a la vista de "trabajador"
        Y ingreso "Loera" en el buscador
        Cuando doy clic en "buscar"
        Entonces puedo ver "Salvador" en la vista de resultados
        Y puedo ver "Juan" en la vista de resultados
        Y puedo ver "Aldonso" en la vista de resultados

    Escenario: Buscar un trabajador con nombre Loe
        Dado que ingreso a la vista de "trabajador"
        Y ingreso "Loe" en el buscador
        Cuando doy clic en "buscar"
        Entonces puedo ver "No hay resultados"
    
    Escenario: Buscar un trabajador con rfc LOQSY32231
        Dado que ingreso a la vista de "trabajador"
        Y ingreso "LOQSY32231" en el buscador
        Cuando doy clic en "buscar"
        Entonces puedo ver "Salvador" en la vista de resultados
    
    Escenario: Buscar un trabajador con rfc LOQS98
        Dado que ingreso a la vista de "trabajador"
        Y ingreso "LOQS98" en el buscador
        Cuando doy clic en "buscar"
        Entonces puedo ver "No hay resultados"

    Escenario: Buscar un trabajador con nombre 
        Dado que ingreso a la vista de "trabajador"
        Y ingreso " " en el buscador
        Cuando doy clic en "buscar"
        Entonces puedo ver "No hay resultados"