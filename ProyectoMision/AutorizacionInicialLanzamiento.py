#====================================================================================

# Archivo: Ejercicio 4: Autorización inicial de lanzamiento
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes:Gerald Alexander Peñaranda Pereira.
# Fecha: 13/09/2026 Versión: 1.0
# Descripción: Verificació inicial para el lanzamiento de la nave con todos los recursos 
# necesarios

#====================================================================================

# Las constantes son datos que no cambian y que el programa utiliza
# para realizar los cálculos necesarios de la misión.

COMBUSTIBLE_RESERVA = 10

# Datos de entrada
# Los datos de entrada son los valores que ingresa el usuario para que el
# programa pueda leerlos y realizar los cálculos correspondientes de oxígeno y recursos requeridos para la misión.

combustible_disponible = int(input("Ingresar combustible disponible de la nave: "))
cantidad_combustible_ida = int(input("Ingresar combustible disponible de ida para la misión: "))
cantidad_combustible_regreso = int(input("Ingresar combustible disponible para el regreso de la misión: "))
cantidad_oxigeno_disponible = int(input("Ingresar la cantidad de oxígeno disponible de la nave: "))
cantidad_oxigeno_requerido = int(input("Ingresar la cantidad requerida de oxígeno para la misión: "))
cantidad_energia_disponible  = int(input("Ingresar la cantidad de energía disponible de la nave: "))
cantidad_energia_requerida = int(input("Ingresar la cantidad de energía requerida para la misión: "))
cantidad_provisiones_disponibles = int(input("Ingresar la cantidad de provisiones disponibles: "))
cantidad_provisiones_requeridas = int(input("Ingresar la cantidad requerida de provisiones para la misión: "))

#Datos proceso
#En esta etapa, el programa realiza los cálculos necesarios para obtener los datos de salida correctos de la misión y utiliza 
#estructuras condicionales para tomar decisiones según las condiciones establecidas, ejecutando la acción correspondiente.

combustible_total_requerido = cantidad_combustible_ida + cantidad_combustible_regreso + COMBUSTIBLE_RESERVA

lanzamiento_autorizado = (combustible_disponible >= combustible_total_requerido and cantidad_oxigeno_disponible >= cantidad_oxigeno_requerido and cantidad_energia_disponible >= cantidad_energia_requerida and cantidad_provisiones_disponibles >= cantidad_provisiones_requeridas)

if lanzamiento_autorizado:
    print("Lanzamiento  autorizado. ")
else:
    print("Lanzamiento no autorizado. La misión debe ser revisada.")