import random 

def juego_adivina_numero(maximo):
    # Paso 1: "pensar" el numero
    numero_secreto = random.randint(1, maximo)
    # Paso 2: pedirle un numero al jugador
    while numero != numero_secreto: #True
        numero = int(input(f"Introduzca un  entre 1 y {maximo}:"))
    
        # Paso 3: 
        #Si el numero es correcto, fin
        if numero_secreto == numero:
            print("Has acertado!")
            #break
        elif numero_secreto > numero:
            #Si el numero introducido es menor o mayor, informas al jugador, e ir al paso 2
            print("El número pensado es mayor")
        elif numero_secreto < numero:
            print("El número pensado es menor")
                
juego_adivina_numero(10)