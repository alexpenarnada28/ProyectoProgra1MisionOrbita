#====================================================================================

# Archivo: VerificaciónCombustible.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Gerald Alexander Peñaranda Pereira.
# Fecha: 10/09/2026 Versión: 1.0
# Descripción: Verificación de combustible.

#====================================================================================

#Constantes del programa
#Las constantes son los datos que no cambian y que el programa utiliza, para poder realizar los cálculos necesarios para la misión.

COMBUSTIBLE_RESERVA = 10
LIMITE_ADVERTENCIA = 10

# Datos de entrada
# Los datos de entrada son los datos que ingresa el usuario, para que el programa reconozca sus necesidades, pueda leerlos,
# y realizar los cálculos correspondientes. 

combustible_disponible = int(input("Ingresar el comustible disponible de la nave: "))
combustible_ida = int(input("Ingresar el combustible requerido para llegar al destino de la misión: "))
combustible_regreso = int(input("Ingresar el combustible requerido para el regreso de la misión: "))

# Datos de proceso
# En esta parte, el programa realiza los cálculos necesarios para obtener los datos de salida correctos para la misión.

combustible_total_requerido = combustible_ida + combustible_regreso + COMBUSTIBLE_RESERVA
combustible_adicional = combustible_disponible - combustible_total_requerido

if combustible_adicional < LIMITE_ADVERTENCIA:
    print("Advertencia: el margen adicional de combustible es bajo.")

# Datos de salida
# En este apartado se muestran los resultados de los datos de proceso y los datos de entrada,
# que le asignamos al programa desde el inicio.

print("Combustible disponible de la nave:", combustible_disponible)
print("Combustible requerido para llegar al destino:", combustible_ida)
print("Combustible requerido para regresar de la misión:", combustible_regreso)
print("Cantidad de combustible adicional:", combustible_adicional)
print("Reserva de emergencia:",COMBUSTIBLE_RESERVA)
print("Combustible total requerido para la misión:", combustible_total_requerido)





