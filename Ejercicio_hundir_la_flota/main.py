# Este va a ser el main
# Lógica de juego

# Importamos las funciones desde el archivo utils.py
from utils import *

# Definimos los parámetros del juego
tamaño_tablero = 10
flota_inicial = 6 # número de barcos que habrá en el tablero al iniciar la partida, no la uso para simplificar

turnos_limite = 3 # 3 turnos max para no alargar la presentación
turno_actual = 1

vidas_jugador = 1 # Quien consiga acertar primero gana
vidas_oponente = 1

#barcos_jugador = flota_inicial
#barcos_oponente = flota_inicial

# Creamos la 'zona' de juego
tablero_oponente = crear_tablero() # Creamos el tablero del oponente

#print(tablero_oponente)
oponente_barco_1 = crear_barco(2) # Creamos los 6 barcos de la flota del oponente
oponente_barco_2 = crear_barco(2)
oponente_barco_3 = crear_barco(2)
oponente_barco_4 = crear_barco(3)
oponente_barco_5 = crear_barco(3)
oponente_barco_6 = crear_barco(4)
#print(f"{oponente_barco_1}\n{oponente_barco_2}\n{oponente_barco_3}\n{oponente_barco_4}\n{oponente_barco_5}\n{oponente_barco_6}")


oponente_coordenadas_1 = colocar_barcos(oponente_barco_1, tablero_oponente) # Colocamos los 6 barcos de la flota del oponente
oponente_coordenadas_2 = colocar_barcos(oponente_barco_2, tablero_oponente)
oponente_coordenadas_3 = colocar_barcos(oponente_barco_3, tablero_oponente)
oponente_coordenadas_4 = colocar_barcos(oponente_barco_4, tablero_oponente)
oponente_coordenadas_5 = colocar_barcos(oponente_barco_5, tablero_oponente)
oponente_coordenadas_6 = colocar_barcos(oponente_barco_6, tablero_oponente)
#print(tablero_oponente)

# Hacemos lo mismo para el jugador
tablero_jugador = crear_tablero() # Creamos el tablero del jugador

#print(tablero_oponente)
jugador_barco_1 = crear_barco(2) # Creamos los 6 barcos de la flota del oponente
jugador_barco_2 = crear_barco(2)
jugador_barco_3 = crear_barco(2)
jugador_barco_4 = crear_barco(3)
jugador_barco_5 = crear_barco(3)
jugador_barco_6 = crear_barco(4)
#print(f"{jugador_barco_1}\n{jugador_barco_2}\n{jugador_barco_3}\n{jugador_barco_4}\n{jugador_barco_5}\n{jugador_barco_6}")


jugador_coordenadas_1 = colocar_barcos(jugador_barco_1, tablero_jugador) # Colocamos los 6 barcos de la flota del oponente
jugador_coordenadas_2 = colocar_barcos(jugador_barco_2, tablero_jugador)
jugador_coordenadas_3 = colocar_barcos(jugador_barco_3, tablero_jugador)
jugador_coordenadas_4 = colocar_barcos(jugador_barco_4, tablero_jugador)
jugador_coordenadas_5 = colocar_barcos(jugador_barco_5, tablero_jugador)
jugador_coordenadas_6 = colocar_barcos(jugador_barco_6, tablero_jugador)
#print(tablero_oponente)

# Empezamos la partida
print(tablero_jugador)
print() # Prints vacios para que sea más legible
print("Empieza el juego")
print()

while vidas_jugador > -1 and vidas_oponente > -1:

    if vidas_jugador == 0:
        print("¡Has perdido!") # Condición de derrota
        print()
        break
    
    else:
        if turno_actual <= turnos_limite: # Mientras no se cumplan, jugamos
            
            print("Elige las coordenadas de tu próximo disparo") # Interfaz de disparo
            print("Introduce un número del 0 al 9:")
            print()
            
            while True: # Esto me lo ha dado ChatGPT porque no conseguía volver al bucle al introducir un valor erroneo
                try:
                    coor_ancho = int(input("A lo ancho\n"))
                    break
                except ValueError:
                    print("Eso no es un número")
                    print()

            while True:
                try:
                    coor_largo = int(input("A lo largo\n"))
                    break
                except ValueError:
                    print("Eso no es un número")
                    print()

            coor_disparo = [coor_ancho, coor_largo]
            print(f"Disparas a las coordenadas: {coor_disparo}")
            print()
            
            disparo = disparar(coor_disparo, tablero_oponente) # Ejecutamos la función de disparo
            print(disparo)
            print()

            if disparo == "Tocado": # Comprobamos si hemos acertado
                vidas_oponente = vidas_oponente -1
                
                if vidas_oponente == 0:
                    print("¡Has ganado!") # Condicón de victoria
                    print()
                    break

            coor_ancho_1 = random.randint(0, 9)
            coor_largo_1 = random.randint(0, 9)
            coor_disparo_1 = [coor_ancho_1, coor_largo_1] 
            
            
            #disparo = disparar([random.randint(0, 9), random.randint(0, 9)], tablero_jugador) # Turno del oponente
            print(f"El oponente dispara a las coordenadas {coor_disparo_1}")
            print()
            print(disparo)
            print()

            if disparo == "Tocado":
                vidas_jugador = vidas_jugador -1

            turno_actual = turno_actual + 1 # Avanzamos de turno

        else:
            print("¡Se acabó el juego!")
            print()
            break