#====================================================================================

# Archivo: Ejercicio 3: Verificación del soporte para la tripulación
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Gerald Alexander Peñaranda Pereira.
# Fecha: 10/09/2026 Versión: 1.0
# Descripción: Verificación del oxígeno y las provisiones necesarias para la tripulación durante el viaje de la misión.

#====================================================================================

# Datos de entrada
# Los datos de entrada son los valores que ingresa el usuario para que el
# programa pueda leerlos y realizar los cálculos correspondientes de oxígeno y recursos requeridos para la misión.

cantidad_oxigeno_disponible = int(input("Ingresar la cantidad de oxígeno disponible en la nave: "))
cantidad_oxigeno_requerido = int(input("Ingresar la cantidad de oxígeno requerido para la misión: "))
cantidad_provisiones_disponibles =int(input("Ingresar la cantidad de provisiones disponible para la misión: "))
cantidad_provisiones_requeridas = int(input("Ingresar las provisiones requeridas para la misión: "))

# Proceso intermedio ejecución.
# En esta etapa se incluyen las estructuras condicionales, que permiten al
# programa tomar decisiones según las condiciones establecidas y ejecutar laacción correspondiente.

if  cantidad_oxigeno_disponible >= cantidad_oxigeno_requerido and cantidad_provisiones_disponibles >= cantidad_provisiones_requeridas:
    mensaje_resultado = "La nave posee recursos suficientes para la tripulación."

else:
     mensaje_resultado = "La nave no posee recursos suficientes para la tripulación."

print(mensaje_resultado)