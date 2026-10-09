#====================================================================================

# Archivo: ejercicio1.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Gerald Alexander Peñaranda Pereira.
# Fecha: 06/09/2026 Versión: 1.0
# Descripción: Calcula los recursos necesarios para una misión.

#====================================================================================

#Constantes del programa
#Las constantes son los datos que no cambian y que el programa utiliza, para poder realizar los cálculos necesarios para la misión.

COMBUSTIBLE_REQUERIDO_DIARIO = 8
COMBUSTIBLE_RESERVA = 10
OXIGENO_RESERVA = 5
OXIGENO_REQUERIDO_DIARIO = 2
ENERGIA_REQUERIDA_DIARIA = 5
ENERGIA_RESERVA = 10
PROVISIONES_RESERVA = 3
TRAMOS_VIAJES = 2

# Datos de entrada
# Los datos de entrada son los datos que ingresa el usuario, para que el programa reconozca sus necesidades, pueda leerlos,
# y realizar los cálculos correspondientes. 

nombre_mision = input("Ingresar el nombre asignado a la misión: ")
cantidad_tripulantes = int(input("Ingresar la cantidad de tripulantes que van a la misión: "))
cantidad_dias_destino = int(input("Ingresar la cantidad de días para la llegada al destino: "))

# Datos de proceso
# En esta parte, el programa realiza los cálculos necesarios para obtener los datos de salida correctos para la misión.

combustible_ida = cantidad_dias_destino * COMBUSTIBLE_REQUERIDO_DIARIO
combustible_regreso = cantidad_dias_destino * COMBUSTIBLE_REQUERIDO_DIARIO
combustible_total_requerido = combustible_ida + combustible_regreso + COMBUSTIBLE_RESERVA
oxigeno_total_requerido = cantidad_dias_destino * OXIGENO_REQUERIDO_DIARIO * TRAMOS_VIAJES * cantidad_tripulantes + OXIGENO_RESERVA
energia_total_requerida = cantidad_dias_destino * ENERGIA_REQUERIDA_DIARIA * TRAMOS_VIAJES + ENERGIA_RESERVA
provisiones_totales_requeridas = cantidad_dias_destino * cantidad_tripulantes * TRAMOS_VIAJES + PROVISIONES_RESERVA

# Datos de salida
# En este apartado se muestran los resultados de los datos de proceso y los datos de entrada,
# que le asignamos al programa desde el inicio.

print("Nombre de la misión:", nombre_mision)
print("Cantidad total de tripulantes:", cantidad_tripulantes)
print("Duración estimada hasta el destino:", cantidad_dias_destino)
print("Combustible requerido para llegar al destino:", combustible_ida)
print("Combustible requerido para regresar de la misión:", combustible_regreso)
print("Reserva de combustible de la nave:", COMBUSTIBLE_RESERVA)
print("Combustible total requerido para la misión:", combustible_total_requerido)
print("Reserva de oxígeno para la misión:", OXIGENO_RESERVA)
print("Oxígeno total requerido para la misión:", oxigeno_total_requerido)
print("Reserva de energía para la misión:", ENERGIA_RESERVA)
print("Energía total requerida para la misión:", energia_total_requerida)
print("Reserva de provisiones para la misión:", PROVISIONES_RESERVA)
print("Provisiones totales para la misión:", provisiones_totales_requeridas)
