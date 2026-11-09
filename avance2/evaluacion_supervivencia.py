# ============================================================
# Archivo: Ejercicio 8 evaluacion_supervivencia.py
# Curso: SOFT-01 Principios 
# Programación 1 - Sección SCV3 / SCV6
# Integrante: Gerald Alexander Peñaranda Pereira
# Fecha: 07/11/2026        Versión: 1.0
# Descripción: Evalúa el regreso de la tripulación y su supervivencia.
# ============================================================


# Constantes de consumo diario.
COMBUSTIBLE_CONSUMO_DIARIO = 8
OXIGENO_CONSUMO_DIARIO = 2
ENERGIA_CONSUMO_DIARIO = 5
PROVISIONES_CONSUMO_DIARIO = 1

# Entrada de datos: estado de la nave al finalizar la exploración.
cantidad_de_tripulantes = int(input("Ingresar la cantidad de tripulantes: "))
cantidad_dias_ida = int(input("Ingresar la cantidad de días del viaje de ida: "))
combustible_disponible = int(input("Ingresar el combustible disponible: "))
oxígeno_disponible = int(input("Ingresar el oxígeno disponible: "))
energia_disponible = int(input("Ingresar la energía disponible: "))
provisiones_disponibles = int(input("Ingresar las provisiones disponibles: "))


# Se determina si existe combustible suficiente para iniciar el regreso.

if  (combustible_disponible >= ( cantidad_dias_ida * COMBUSTIBLE_CONSUMO_DIARIO) ):
    # Caso A: simulación diaria del regreso.
    dia_actual = 1

    # Esta variable es una bandera que interrumpe el ciclo cuando alguno de los suministeros es menor qur 0 
    bandera_interrumpir = True

    while(dia_actual <= cantidad_dias_ida and bandera_interrumpir ):

        if (combustible_disponible < COMBUSTIBLE_CONSUMO_DIARIO) or  (oxígeno_disponible < OXIGENO_CONSUMO_DIARIO * cantidad_de_tripulantes) or (energia_disponible < ENERGIA_CONSUMO_DIARIO) or (provisiones_disponibles < PROVISIONES_CONSUMO_DIARIO * cantidad_de_tripulantes):
            print(f"\nEl regreso se interrumpió en el día {dia_actual}.")

            if combustible_disponible < COMBUSTIBLE_CONSUMO_DIARIO:
                print("Recurso insuficiente: Combustible")
            if oxígeno_disponible < OXIGENO_CONSUMO_DIARIO * cantidad_de_tripulantes:
                print("Recurso insuficiente: Oxígeno")
            if energia_disponible < ENERGIA_CONSUMO_DIARIO:
                print("Recurso insuficiente: Energía")
            if provisiones_disponibles < PROVISIONES_CONSUMO_DIARIO * cantidad_de_tripulantes:
                print("Recurso insuficiente: Provisiones")

            print("La tripulación no completó el regreso.")
            bandera_interrumpir = False
        
        else:
            combustible_disponible = combustible_disponible - COMBUSTIBLE_CONSUMO_DIARIO
            oxígeno_disponible = oxígeno_disponible - ( OXIGENO_CONSUMO_DIARIO * cantidad_de_tripulantes)
            energia_disponible = energia_disponible - ENERGIA_CONSUMO_DIARIO
            provisiones_disponibles = provisiones_disponibles -  (PROVISIONES_CONSUMO_DIARIO * cantidad_de_tripulantes)

            print( f"\nDía {dia_actual} | Combustible: {combustible_disponible} | Oxígeno: {oxígeno_disponible} | Energía: {energia_disponible} | Provisiones: {provisiones_disponibles}" )
            dia_actual = dia_actual + 1


    if bandera_interrumpir:
        print("\nLa tripulación regresó exitosamente a la Tierra.")  
        print(f"Combustible restante: {combustible_disponible} unidades")
        print(f"Oxígeno restante: {oxígeno_disponible} unidades")
        print(f"Energía restante: {energia_disponible} unidades")
        print(f"Provisiones restantes: {provisiones_disponibles} unidades")


   
    
# Caso B: cálculo de supervivencia cuando la tripulación queda varada.
else:
    print("\nLa tripulación quedó varada en el destino.")
    
    dias_oxigeno = oxígeno_disponible // (cantidad_de_tripulantes * OXIGENO_CONSUMO_DIARIO)
    dias_energia = energia_disponible // ENERGIA_CONSUMO_DIARIO
    dias_provisiones = provisiones_disponibles // cantidad_de_tripulantes


    print("\nDías por oxígeno:", dias_oxigeno)
    print("Días por energía:",dias_energia)
    print("Días por provisiones:",dias_provisiones)

    if (dias_oxigeno <= dias_energia and dias_oxigeno <= dias_provisiones):
        supervivencia_estimada = dias_oxigeno
     
    elif ( dias_energia <= dias_oxigeno and dias_energia <= dias_provisiones):
        supervivencia_estimada = dias_energia
        
    elif (dias_provisiones <= dias_oxigeno and dias_provisiones <= dias_energia):
        supervivencia_estimada = dias_provisiones
   


    print("Supervivencia estimada:", supervivencia_estimada, "días")

    recursos_limitantes = ""

    if dias_oxigeno == supervivencia_estimada:

        #Agregar el oxigeno como recurso limitante.
        recursos_limitantes = "oxígeno"

    if dias_energia == supervivencia_estimada:
        #Hacer que aparezca la coma bonito. 
        if recursos_limitantes != "":
            recursos_limitantes = recursos_limitantes + ", "

        #Agregar la energia como recurso limitante.
        recursos_limitantes = recursos_limitantes + "energía"

    if dias_provisiones == supervivencia_estimada:
        #Hacer que aparezca la coma bonito. 
        if recursos_limitantes != "":
            recursos_limitantes = recursos_limitantes + ", "
        #Agregar las provisiones como recurso limitante.
        recursos_limitantes = recursos_limitantes + "provisiones"

    print("Recurso(s) limitante(s):", recursos_limitantes)



     
    
  
