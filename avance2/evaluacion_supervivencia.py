
#Caso A #1:
# cantidad_de_tripulantes = 2
# cantidad_dias_ida = 3
# combustible_disponible = 30
# oxígeno_disponible = 20
# energia_disponible = 20
# provisiones_disponibles = 10

#Caso A #2:

# cantidad_de_tripulantes = 2
# cantidad_dias_ida = 3
# combustible_disponible = 30
# oxígeno_disponible = 10
# energia_disponible = 20
# provisiones_disponibles = 10


#Caso B:
cantidad_de_tripulantes = 2
cantidad_dias_ida = 5
combustible_disponible = 10
oxígeno_disponible = 20
energia_disponible = 25
provisiones_disponibles = 12

# Constantes 
COMBUSTIBLE_CONSUMO_DIARIO = 8
OXIGENO_CONSUMO_DIARIO = 2
ENERGIA_CONSUMO_DIARIO = 5
PROVISIONES_CONSUMO_DIARIO = 1



switchCaso = (combustible_disponible >= ( cantidad_dias_ida * COMBUSTIBLE_CONSUMO_DIARIO) )

if switchCaso:
   
    dia_actual = 1

    # Esta variable es una bandera que interrumpe el ciclo cuando alguno de los suministeros es menor qur 0 
    bandera_interrumpir = True

    while(dia_actual <= cantidad_dias_ida and bandera_interrumpir ):

        if (combustible_disponible < COMBUSTIBLE_CONSUMO_DIARIO) or  (oxígeno_disponible < OXIGENO_CONSUMO_DIARIO * cantidad_de_tripulantes) or (energia_disponible < ENERGIA_CONSUMO_DIARIO) or (provisiones_disponibles < PROVISIONES_CONSUMO_DIARIO * cantidad_de_tripulantes):
            print("El regreso se interrumpió en el día", dia_actual)

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

            print( f"Día {dia_actual} | Combustible: {combustible_disponible} |Oxígeno {oxígeno_disponible} | Energía {energia_disponible} |  Provisiones {provisiones_disponibles}" )
            dia_actual = dia_actual + 1


    if bandera_interrumpir:
        print("La tripulación regresó exitosamente a la Tierra.")  
        print(f"Combustibe restante: {combustible_disponible} unidades.")
        print(f"Oxígeno restante: {oxígeno_disponible} unidades.")
        print(f"Energía restante: {energia_disponible} unidades.")
        print(f"Provisiones restante: {provisiones_disponibles} unidades")


   
    
else: 
    print("La tripulación quedó varada en el destino.")
    
    dias_oxigeno = oxígeno_disponible // (cantidad_de_tripulantes * 2)
    dias_energia = energia_disponible // 5
    dias_provisiones = provisiones_disponibles // cantidad_de_tripulantes

    if (dias_oxigeno <= dias_energia and dias_oxigeno <= dias_provisiones):
        supervivencia_estimada = dias_oxigeno
     
    elif ( dias_energia <= dias_oxigeno and dias_energia <= dias_provisiones):
        supervivencia_estimada = dias_energia
        
    elif (dias_provisiones <= dias_oxigeno and dias_provisiones <= dias_energia):
        supervivencia_estimada = dias_provisiones
   


    
   
    print("Días por oxígeno:", dias_oxigeno)
    print("Días por energía:",dias_energia)
    print("Días por provisiones:",dias_provisiones)

    menor = 0
    if dias_oxigeno <= dias_energia and dias_oxigeno <= dias_provisiones:
        menor = dias_oxigeno
    elif dias_energia <= dias_oxigeno and dias_energia <= dias_provisiones:
        menor = dias_energia
    else:
        menor = dias_provisiones

    print("Supervivencia estimada:", menor)

    recursos_limitantes = ""

    if dias_oxigeno == menor:

        #Agregar el oxigeno como recurso limitante.
        recursos_limitantes = "oxígeno"

    if dias_energia == menor:
        #Hacer que aparezca la coma bonito. 
        if recursos_limitantes != "":
            recursos_limitantes = recursos_limitantes + ", "

        #Agregar la energia como recurso limitante.
        recursos_limitantes = recursos_limitantes + "energía"

    if dias_provisiones == menor:
        #Hacer que aparezca la coma bonito. 
        if recursos_limitantes != "":
            recursos_limitantes = recursos_limitantes + ", "
        #Agregar las provisiones como recurso limitante.
        recursos_limitantes = recursos_limitantes + "provisiones"

    print("Recurso(s) limitante(s):", recursos_limitantes)



     
    
  
