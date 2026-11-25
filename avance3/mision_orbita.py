
COMBUSTIBLE_REQUERIDO_DIARIO = 8
COMBUSTIBLE_RESERVA = 10
OXIGENO_RESERVA = 5
OXIGENO_REQUERIDO_DIARIO = 2
ENERGIA_REQUERIDA_DIARIA = 5
ENERGIA_RESERVA = 10
PROVISIONES_RESERVA = 3
TRAMOS_VIAJES = 2
DESTINOS = (("Luna", 3), ("Marte", 5), ("Europa", 7))
RECURSOS = ("combustible", "oxígeno", "energía", "provisiones")
COMBUSTIBLE = 0
LIMITE_ADVERTENCIA = 10





def ejecutar_mision(numero):
    print("=== PLANIFICACIÓN ===")

    nombre_mision = input("Nombre de la misión: ")
    cantidad_tripulantes = int(input("Cantidad de tripulantes: "))

    mostrar_destinos()
    opcion_destino = int(input("Seleccione un destino: "))

    if opcion_destino < 1 or opcion_destino > len(DESTINOS):
        print("Opción de destino no válida. La misión no puede planificarse.")
    else:
        destino = DESTINOS[opcion_destino - 1]
        nombre_destino = destino[0]
        dias_viaje = destino[1]
        disponibles = leer_recursos()
        requeridos = calcular_requeridos(dias_viaje, cantidad_tripulantes)

        mostrar_resumen (nombre_mision,nombre_destino,dias_viaje,cantidad_tripulantes,disponibles,requeridos)
        lanzamiento_autorizado = autorizar_lanzamiento(disponibles, requeridos)
        if lanzamiento_autorizado:
            print("Lanzamiento autorizado.")
        else:
            print("Lanzamiento no autorizado. La misión debe ser revisada.")
 # i indice     

def mostrar_destinos():

    print("Destinos disponibles:")

    for i in range(len(DESTINOS)):
        destino = DESTINOS[i]
        print(f"{i + 1}. {destino[0]} ({destino[1]} días)")



def leer_recursos():
    disponibles = []

    for recurso in RECURSOS:
        cantidad = int(input(f"Cantidad disponible de {recurso}: "))
        disponibles.append(cantidad)

    return disponibles
    
def calcular_requeridos(dias_viaje, tripulantes):

    combustible_ida = dias_viaje * COMBUSTIBLE_REQUERIDO_DIARIO
    combustible_regreso = dias_viaje * COMBUSTIBLE_REQUERIDO_DIARIO
    combustible_total_requerido = combustible_ida + combustible_regreso + COMBUSTIBLE_RESERVA
    oxigeno_total_requerido = dias_viaje * OXIGENO_REQUERIDO_DIARIO * TRAMOS_VIAJES * tripulantes + OXIGENO_RESERVA
    energia_total_requerida = dias_viaje * ENERGIA_REQUERIDA_DIARIA * TRAMOS_VIAJES + ENERGIA_RESERVA
    provisiones_totales_requeridas = dias_viaje * tripulantes * TRAMOS_VIAJES + PROVISIONES_RESERVA

    requeridos = [combustible_total_requerido, oxigeno_total_requerido, energia_total_requerida, provisiones_totales_requeridas]

    return requeridos



def mostrar_resumen(nombre_mision,nombre_destino,dias_viaje,tripulantes,disponibles,requeridos):
    
    print(f"Mison: {nombre_mision} ")
    print(f"Destino: {nombre_destino} ")
    print(f"Duración del viaje de ida: {dias_viaje} días ")
    print(f"Tripulantes: {tripulantes} ")

    for i in range (len(RECURSOS)):
            recuersos = RECURSOS [i].capitalize()
            print(recuersos, "Disponibles:", disponibles[i], "Requeridos:", requeridos[i])
    margen_combustible = disponibles[0] - requeridos[0]
    print("Margen adicional de combustible:", margen_combustible)
    if margen_combustible < 10:
     print("Advertencia: el margen de combustible es menor que 10.")

def autorizar_lanzamiento(disponible,requerido):

    autorizar_lanzamiento = True

    for i in range(len(disponible)):
        if disponible[i] < requerido[i]:
            autorizar_lanzamiento = False

    return autorizar_lanzamiento  


def simular_trayecto(dias_viaje, tripulantes, recursos):
    print("=== VIAJE DE IDA ===")

    
