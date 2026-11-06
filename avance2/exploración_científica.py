#====================================================================================

# Archivo: ejercicio7_exploracion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrante: Gerald Alexander Peñaranda Pereira
# Fecha: 30/11/2026
# Versión: 1.0
# Descripción: Simula las actividades de exploración científica de la nave.

#====================================================================================

# Constantes del programa
# Las constantes son los datos que no cambian y que el programa utiliza, para poder realizar los cálculos necesarios para la misión.

ANALIZAR_TERRENO_ENERGIA = 8
ANALIZAR_TERRENO_PROVISIONES = 0
RECOLECTAR_MUESTRA_ENERGIA = 12
RECOLECTAR_MUESTRA_PROVISIONES = 2
REALIZAR_OBSERVACION_ENERGIA = 5
REALIZAR_OBSERVACION_PROVISIONES = 0
PUNTOS_ANALIZAR_TERRENO = 10
PUNTOS_RECOLECTAR_MUESTRA = 20
PUNTOS_REALIZAR_OBSERVACION = 8

# Variables iniciales
# Estas variables empiezan en cero y se van actualizando durante
# la exploración científica.

puntos_cientificos = 0
actividades_realizadas = 0
muestras_recolectadas = 0
energia_disponible_destino = 0
provisiones_disponibles_destino = 0


#Datos de entrada
# Los datos de entrada son los datos que ingresa el usuario, para que el programa reconozca sus necesidades, pueda leerlos,
# y realizar los cálculos correspondientes. 

energia_disponible_destino = int(input("Ingresar la energía disponible: "))
provisiones_disponibles_destino = int(input("Ingresar las provisiones disponibles: "))

#Continúa con la ejecución del programa ingresando al menú, se mantiene activo durante la exploración hasta que el usuario
# finaliza o los recursos son insuficientes.

menu_activo = True

while menu_activo:
    
    print("1. Analizar terreno")
    print("2. Recolectar muestra")
    print("3. Realizar observación")
    print("4. Finalizar exploración")

    opcion = input("Seleccione una actividad: ")

    if opcion == "1":
          
        if (energia_disponible_destino >= ANALIZAR_TERRENO_ENERGIA) and (provisiones_disponibles_destino >= ANALIZAR_TERRENO_PROVISIONES):
            energia_disponible_destino = (energia_disponible_destino) - (ANALIZAR_TERRENO_ENERGIA)
            provisiones_disponibles_destino = (provisiones_disponibles_destino) - (ANALIZAR_TERRENO_PROVISIONES)
            actividades_realizadas = actividades_realizadas + 1
            puntos_cientificos = puntos_cientificos + PUNTOS_ANALIZAR_TERRENO

            print("Actividad realizada: Analizar terreno. Puntos obtenidos: 10")
            
        else:
            menu_activo = False
            print ("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
    
    elif opcion == "2":
        
        if (energia_disponible_destino >= RECOLECTAR_MUESTRA_ENERGIA) and (provisiones_disponibles_destino >= RECOLECTAR_MUESTRA_PROVISIONES):
            energia_disponible_destino = (energia_disponible_destino) - (RECOLECTAR_MUESTRA_ENERGIA)
            provisiones_disponibles_destino = (provisiones_disponibles_destino) - (RECOLECTAR_MUESTRA_PROVISIONES)
            actividades_realizadas = actividades_realizadas + 1
            puntos_cientificos = puntos_cientificos + PUNTOS_RECOLECTAR_MUESTRA
            muestras_recolectadas = muestras_recolectadas + 1

            print("Actividad realizada: Recolectar muestra. Puntos obtenidos: 20")
            
        else:
            menu_activo = False
            print ("Recursos insuficientes para realizar la actividad. La exploración finaliza.")


    elif opcion == "3":
        
        if (energia_disponible_destino >= REALIZAR_OBSERVACION_ENERGIA) and (provisiones_disponibles_destino >= REALIZAR_OBSERVACION_PROVISIONES):
            
            energia_disponible_destino =  energia_disponible_destino - REALIZAR_OBSERVACION_ENERGIA
            provisiones_disponibles_destino = provisiones_disponibles_destino - REALIZAR_OBSERVACION_PROVISIONES
            actividades_realizadas = actividades_realizadas + 1
            puntos_cientificos = puntos_cientificos + PUNTOS_REALIZAR_OBSERVACION
            

            print("Actividad realizada: Realizar observación. Puntos obtenidos: 8")
            
        else:
            menu_activo = False
            print ("Recursos insuficientes para realizar la actividad. La exploración finaliza.")


    elif opcion == "4":
        print("Exploración finalizada por la tripulación.")
        menu_activo = False
        
    else:
        print("\nOpción no válida.\n")

#Finalizar exploración, se desactiva el menú y se muestra el resumen final.

print("Actividades realizadas: ",actividades_realizadas)
print("Muestras recolectadas: ",muestras_recolectadas)
print("Puntos científicos: ",puntos_cientificos)
print(f"Energía restante: {energia_disponible_destino} unidades")
print(f"Provisiones restantes: {provisiones_disponibles_destino} unidades")


    









    
    