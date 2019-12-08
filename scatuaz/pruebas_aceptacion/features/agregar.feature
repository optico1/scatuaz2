Característica: Creación de un trabajador
    Como usuario del sistema SCATUAZ, quiero crear(dar de alta) un trabajador.

    Escenario: Crear un trabajador con campos obligatorios completos
        Dado    que ingreso al formulario para llenar los datos del trabajador
        Y escribo los datos: "Salvador", "Loera", "Quiroz", "VECJ880326 XXX", "BEMF980417MZSRRT06"
        Cuando de clic en el botón crear trabajador
        Entonces podré ver el trabajador "Loera" en la lista de trabajador


    Escenario: Crear un trabajador con campos obligatorios completos invalidos
        Dado    que ingreso al formulario para llenar los datos del trabajador
        Y escribo los datos: "Fatima", "Berumen", "Murillo", "VECJXX", "BEMF9sdfsdf17MZSRRT06"
        Cuando de clic en el botón crear trabajador
        Entonces no podré ver el trabajador "Berumen" en la lista de trabajador



    Escenario: Crear un trabajador con campos obligatorios incompletos 
        Dado    que ingreso al formulario para llenar los datos del trabajador
        Y escribo los datos: " ", "Berumen", "Murillo", " ", " "
        Cuando de clic en el botón crear trabajador
        Entonces no podré ver el trabajador "Berumen" en la lista de trabajador

    Escenario: Crear un trabajador con campos unicos duplicados
        Dado    que ingreso al formulario para llenar los datos del trabajador
        Y escribo los datos: "Salvador", "Loera", "Quirpz", "VECJ880326 XXX", "BEMF980417MZSRRT06"
        Cuando de clic en el botón crear trabajador
        Entonces podré ver el mensaje de "Trabajador with this Curp already exists."