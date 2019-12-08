   Característica: Eliminar Trabajador
    Como usuario del sistema SCATUAZ
    Quiero eliminar un Trabajador del inventario
    Porque ya no deseo tenerlo en la lista de trabajadores 
    
    Escenario: Eliminar un trabajador correctamente
    	Dado Que ingreso a la lista de los trabajadores
        Y encuentro al trabajador "pedro"
        Cuando presiono el botón eliminar 
        Y confirmo la eliminación en la segunda pantalla
        Entonces ya no puedo ver el trabajador "pedro" en la lista de trabajadores.