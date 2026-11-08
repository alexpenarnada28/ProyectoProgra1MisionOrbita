
#Caso A #1:
cantidad_de_tripulantes = 2
cantidad_dias_ida = 3
combustible_disponible = 30
oxígeno_disponible = 20
energia_disponible = 20
provisiones_disponibles = 10

#Caso A #2:

# cantidad_de_tripulantes = 2
# cantidad_dias_ida = 3
# combustible_disponible = 30
# oxígeno_disponible = 10
# energia_disponible = 20
# provisiones_disponibles = 10


#Caso B:
# cantidad_de_tripulantes = 2
# cantidad_dias_ida = 5
# combustible_disponible = 10
# oxígeno_disponible = 20
# energia_disponible = 25
# provisiones_disponibles = 12

# Constantes 
COMBUSTIBLE_CONSUMO_DIARIO = 8
OXIGENO_CONSUMO_DIARIO = 2
ENERGIA_CONSUMO_DIARIO = 5
PROVISIONES_CONSUMO_DIARIO = 1

switchCaso = (combustible_disponible >= ( cantidad_dias_ida * COMBUSTIBLE_CONSUMO_DIARIO) )

if switchCaso:
    print("Caso A")
    dia_actual = 1
    interrumpir = True

    while(dia_actual <= cantidad_dias_ida and interrumpir ):

        if ( 0 >=  combustible_disponible - COMBUSTIBLE_CONSUMO_DIARIO ) or  (0 >= oxígeno_disponible - ( OXIGENO_CONSUMO_DIARIO * cantidad_de_tripulantes)) or (0 >= energia_disponible - ENERGIA_CONSUMO_DIARIO) or ( 0 >= provisiones_disponibles -  (PROVISIONES_CONSUMO_DIARIO * cantidad_de_tripulantes)):
            print("Fallo en el dia: ", dia_actual)
            interrumpir = False
        else:
            combustible_disponible = combustible_disponible - COMBUSTIBLE_CONSUMO_DIARIO
            oxígeno_disponible = oxígeno_disponible - ( OXIGENO_CONSUMO_DIARIO * cantidad_de_tripulantes)
            energia_disponible = energia_disponible - ENERGIA_CONSUMO_DIARIO
            provisiones_disponibles = provisiones_disponibles -  (PROVISIONES_CONSUMO_DIARIO * cantidad_de_tripulantes)

            print( f"Día {dia_actual} | Combustible: {combustible_disponible} |Oxígeno {oxígeno_disponible} | Energía {energia_disponible} |  Provisiones {provisiones_disponibles}" )
            dia_actual = dia_actual + 1
            

    if interrumpir:
        print("La tripulación regresó exitosamente a la Tierra.")  
        print(f"Combustibe restante: {combustible_disponible} unidades.")
        print(f"Oxígeno restante: {oxígeno_disponible} unidades.")
        print(f"Energía restante: {energia_disponible} unidades.")
        print(f"Provisiones restante: {provisiones_disponibles} unidades")
    else: 
        print("El regreso se interrumpió en el día: ", dia_actual)

   
    
else:
    print("Caso B")