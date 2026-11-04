#====================================================================================

# Archivo: exploración_científica
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Gerald Alexander Peñaranda Pereira.
# Fecha: 30/11/2026 Versión: 1.0
# Descripción: Exploración cientifica 

#====================================================================================

# Constantes del programa
# Las constantes son los datos que no cambian y que el programa utiliza, para poder realizar los cálculos necesarios para la misión.

ANALIZAR_TERRENO_ENERGIA = 8
ANALIZAR_TERRENO_PROVICIONES = 0
RECOLECTAR_MUESTRAS_ENERGIA = 12
RECOLECTAR_MUESTRAS_PROVICIONES = 2
REALIZAR_OBSERVACIONES_ENERGIA = 5
REALIZAR_OBSERVACIONES_PROVICIONES = 0

#Datos de entrada
# Los datos de entrada son los datos que ingresa el usuario, para que el programa reconozca sus necesidades, pueda leerlos,
# y realizar los cálculos correspondientes. 

puntos_cientificos = 0
actividades_realizadas = 0
muestras_recolectadas = 0
energia_disponible_destino = 0
proviciones_disponibles_destino = 0

energia_disponible_destino = int(input(" Ingresar la energía disponible: "))
proviciones_disponibles_destino = int(input(" Ingresar las proviciones disponibles: "))
menu_activo = input("¿Desea iniciar la exploración científica ? (si/no): ").lower() == "si"

#Continúa con la ejecución del programa utilizando los datos ingresados por el usuario.

fin_eject = True

while menu_activo and fin_eject:
    
    
    print("1. Analizar terreno")
    print("2. Recolectar muestra")
    print("3. Realizar observación")
    print("4. Finalizar exploración")

    opcion = int(input("Seleccione una actividad: "))

    if opcion == 1:
        print("1. Analizar terreno")
        
        if (energia_disponible_destino >= ANALIZAR_TERRENO_ENERGIA) and (proviciones_disponibles_destino >= ANALIZAR_TERRENO_PROVICIONES):
            energia_disponible_destino = (energia_disponible_destino) - (ANALIZAR_TERRENO_ENERGIA)
            proviciones_disponibles_destino = (proviciones_disponibles_destino) - (ANALIZAR_TERRENO_PROVICIONES)
            actividades_realizadas = actividades_realizadas + 1
            puntos_cientificos = puntos_cientificos + 10

            print("Actividad realizada: Analizar terreno.")
            print("Puntos obtenidos: 10")
        
        else:
            fin_eject = False
            print ("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
    
    elif opcion == 2:
        print("2. Recolectar muestra")

        if (energia_disponible_destino >= RECOLECTAR_MUESTRAS_ENERGIA) and (proviciones_disponibles_destino >= RECOLECTAR_MUESTRAS_PROVICIONES):
            energia_disponible_destino = (energia_disponible_destino) - (RECOLECTAR_MUESTRAS_ENERGIA)
            proviciones_disponibles_destino = (proviciones_disponibles_destino) - (RECOLECTAR_MUESTRAS_PROVICIONES)
            actividades_realizadas = actividades_realizadas + 1
            puntos_cientificos = puntos_cientificos + 20
            muestras_recolectadas = muestras_recolectadas + 1

            print("Actividad realizada: Recolectar muestras")
            print("Puntos obtenidos: 20")

        else:
            fin_eject = False
            print ("Recursos insuficientes para realizar la actividad. La exploración finaliza.")


    elif opcion == 3:
        print("3. Realizar observación")

        if (energia_disponible_destino >= REALIZAR_OBSERVACIONES_ENERGIA) and (proviciones_disponibles_destino >= REALIZAR_OBSERVACIONES_PROVICIONES):
            actividades_realizadas = actividades_realizadas + 1
            puntos_cientificos = puntos_cientificos + 8

            print("Actividad realizada: Realizar observación")
            print("Puntos obtenidos: 8")

        else:
            fin_eject = False
            print ("Recursos insuficientes para realizar la actividad. La exploración finaliza.")


    elif opcion == 4:
        print("Exploración finalizada por la tripulación.")
        fin_eject = False
        
    else:
        print("\nOpción no válida\n")

print("Actividades realizadas: ", actividades_realizadas)
print("Muestras recolectadas: ", muestras_recolectadas)
print("Puntos científicos: ", puntos_cientificos)
print("Energía restante: ", energia_disponible_destino)
print("Provisiones restantes:", proviciones_disponibles_destino)


    









    
    