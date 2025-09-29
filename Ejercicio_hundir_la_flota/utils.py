# Importamos 
import numpy as np
import random


# Creamos la afunción crear tablero
def crear_tablero(tamaño_tablero:int=10):
    
    return np.full((tamaño_tablero,tamaño_tablero),"_")


# Creamos la función encargada de crear barcos
def crear_barco(eslora:int, tamaño_tablero:int=10):
    
    # Asignamos de forma aleatoria si la alineación del barco es vertical u horizontal
    direccion = random.choice(["horizontal", "vertical"]) 
    
    if direccion == "horizontal":
        fila = random.randint(1, tamaño_tablero -1)
        columna_inicial = random.randint(1, tamaño_tablero - eslora)
        barco = [(fila, columna_inicial + i) for i in range(eslora)]
      
    
    else:
        fila_inicial = random.randint(1, tamaño_tablero - eslora)
        columna = random.randint(1, tamaño_tablero -1)
        barco = [(fila_inicial + i, columna) for i in range(eslora)]

    return barco


# Creamos la función encargada de colocar los barcos creados en el tablero
def colocar_barcos(barco, tablero):
    
    for casilla in barco:
        fila, columna = casilla
        
        if tablero[fila, columna] != "O":
            tablero[fila, columna] = "O"

    return tablero


# Creamos la función encargada de disparar
def disparar(casilla, tablero):
    
    fila, columna = casilla
    if tablero[fila, columna] == "O":
        tablero[fila, columna] = "X"
        return "Tocado"
    else:
        tablero[fila, columna] = "A"
        return "Agua"  


# Esta función permite 'refrescar' el terminal para que no se acumulen los output (?)
# def clear():
    # Works on Windows (cls) and Unix (clear)
#   os.system('cls' if os.name == 'nt' else 'clear')