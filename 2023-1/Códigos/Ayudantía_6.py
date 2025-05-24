#Conecta 4
import numpy as np
#Crear tablero
tablero = np.zeros((6,7), dtype=int)
Game=1
#Empezar juego
while Game==1:
    print(tablero)
    #Preguntarle pos de ficha al jugador 1
    columna=int(input("Jugador 1: Ingrese la columna donde desea la ficha (0, 6): "))
    for fila in range(5, -1, -1):
        if tablero[fila][columna]==0:
            tablero[fila][columna]=1
            break
    #Verificar si gano
    for fila in range(6):
        for columna in range(4):
            if tablero[fila][columna]==tablero[fila][columna+1]==tablero[fila][columna+2]==tablero[fila][columna+3]==1:
                Game="Ganador jugador 1"
                break
    for fila in range(3):
        for columna in range(7):
            if tablero[fila][columna]==tablero[fila+1][columna]==tablero[fila+2][columna]==tablero[fila+3][columna]==1:
                Game="Ganador jugador 1"
                break
    for fila in range(3):
        for columna in range(4):
            if tablero[fila][columna]==tablero[fila+1][columna+1]==tablero[fila+2][columna+2]==tablero[fila+3][columna+3]==1:
                Game="Ganador jugador 1"
                break
    for fila in range(3, 6):
        for columna in range(4):
            if tablero[fila][columna]==tablero[fila-1][columna+1]==tablero[fila-2][columna+2]==tablero[fila-3][columna+3]==1:
                Game="Ganador jugador 1"
                break
    if Game==1:
        print(tablero)
        #Preguntarle pos de ficha al jugador 2
        columna=int(input("Jugador 2: Ingrese la columna donde desea la ficha (0, 6): "))
        for fila in range(5, -1, -1):
            if tablero[fila][columna]==0:
                tablero[fila][columna]=2
                break
        #Verificar si gano
        for fila in range(6):
            for columna in range(4):
                if tablero[fila][columna]==tablero[fila][columna+1]==tablero[fila][columna+2]==tablero[fila][columna+3]==2:
                    Game="Ganador jugador 2"
                    break
        for fila in range(3):
            for columna in range(7):
                if tablero[fila][columna]==tablero[fila+1][columna]==tablero[fila+2][columna]==tablero[fila+3][columna]==2:
                    Game="Ganador jugador 2"
                    break
        for fila in range(3):
            for columna in range(4):
                if tablero[fila][columna]==tablero[fila+1][columna+1]==tablero[fila+2][columna+2]==tablero[fila+3][columna+3]==2:
                    Game="Ganador jugador 2"
                    break
        for fila in range(3, 6):
            for columna in range(4):
                if tablero[fila][columna]==tablero[fila-1][columna+1]==tablero[fila-2][columna+2]==tablero[fila-3][columna+3]==2:
                    Game="Ganador jugador 2"
                    break
    #Verificar el empeta
    if np.sum(tablero==0) == 0:
        Game="Empate"
print(tablero)
print(Game)