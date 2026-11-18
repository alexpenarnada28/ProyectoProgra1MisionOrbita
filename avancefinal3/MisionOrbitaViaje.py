
COMBUSTIBLE_REQUERIDO_DIARIO = 8
COMBUSTIBLE_RESERVA = 10
OXIGENO_RESERVA = 5
OXIGENO_REQUERIDO_DIARIO = 2
ENERGIA_REQUERIDA_DIARIA = 5
ENERGIA_RESERVA = 10
PROVISIONES_RESERVA = 3
TRAMOS_VIAJES = 2


def calcular_requeridos(dias_viaje, tripulantes):

    combustible_ida = dias_viaje * COMBUSTIBLE_REQUERIDO_DIARIO
    combustible_regreso = dias_viaje * COMBUSTIBLE_REQUERIDO_DIARIO
    combustible_total_requerido = combustible_ida + combustible_regreso + COMBUSTIBLE_RESERVA
    oxigeno_total_requerido = dias_viaje * OXIGENO_REQUERIDO_DIARIO * TRAMOS_VIAJES * tripulantes + OXIGENO_RESERVA
    energia_total_requerida = dias_viaje * ENERGIA_REQUERIDA_DIARIA * TRAMOS_VIAJES + ENERGIA_RESERVA
    provisiones_totales_requeridas = dias_viaje * tripulantes * TRAMOS_VIAJES + PROVISIONES_RESERVA

    requeridos = [combustible_total_requerido, oxigeno_total_requerido, energia_total_requerida, provisiones_totales_requeridas]

    return requeridos

print(calcular_requeridos(3, 2))


    
