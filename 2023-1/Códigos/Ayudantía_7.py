import numpy as np
import matplotlib.pyplot as plt

#Solucion prueba simulacro

#Francia
#Generamos 3 matrices, una para R, otra para G y otra para B
matriz_R=np.full((18,27),0)
matriz_G=np.full((18,27),0)
matriz_B=np.full((18,27),0)

#Rellenamos el primer tercio (horizontal) con azul
for azul in range(0,9):
    matriz_R[:,azul]=0
    matriz_G[:,azul]=38
    matriz_B[:,azul]=84

#Rellenamos la segunda parte con blanco
for blanco in range(9,18):
    matriz_R[:,blanco]=255
    matriz_G[:,blanco]=255
    matriz_B[:,blanco]=255

#Rellenamos la tercera parte con rojo
for rojo in range(18,27):
    matriz_R[:,rojo]=237
    matriz_G[:,rojo]=41
    matriz_B[:,rojo]=57

print(matriz_R)

"""
#Para visualizar la bandera (no es necesario saberlo para la prueba)
import matplotlib.pyplot as plt
rgb_image = np.dstack((matriz_R, matriz_G, matriz_B))
plt.imshow(rgb_image)
plt.axis('off')
plt.show()"""

#Rusia
#Generamos 3 matrices, una para R, otra para G y otra para B
matriz_R=np.full((18,27),0)
matriz_G=np.full((18,27),0)
matriz_B=np.full((18,27),0)

#Rellenamos el primer tercio (vertical) con blanco
for blanco in range(0,6):
    matriz_R[blanco,:]=255
    matriz_G[blanco,:]=255
    matriz_B[blanco,:]=255

#Rellenamos el medio con azul
for azul in range(6,12):
    matriz_R[azul,:]=28
    matriz_G[azul,:]=53
    matriz_B[azul,:]=120

#Rellenamos el final con rojo
for rojo in range(12,18):
    matriz_R[rojo,:]=228
    matriz_G[rojo,:]=24
    matriz_B[rojo,:]=28

print(matriz_R)

"""
#Para visualizar la bandera (no es necesario saberlo para la prueba)
import matplotlib.pyplot as plt
rgb_image = np.dstack((matriz_R, matriz_G, matriz_B))
plt.imshow(rgb_image)
plt.axis('off')
plt.show()"""

#Sudoku
#Generamos el rablero 9x9 vacio
tablero=np.zeros((9,9), dtype=int)
print(tablero)

#Rellenamos segun la imagen
tablero[0,0]=5
tablero[1,0]=6
tablero[0,1]=3
tablero[2,1]=9
tablero[2,2]=8
tablero[1,3]=1
tablero[1,4]=9
tablero[1,5]=5
tablero[0,4]=7
tablero[2,7]=6

tablero[3,0]=8
tablero[4,0]=4
tablero[5,0]=7
tablero[3,4]=6
tablero[4,3]=8
tablero[4,5]=3
tablero[5,4]=2
tablero[3,8]=3
tablero[4,8]=1
tablero[5,8]=6

tablero[6,1]=6
tablero[7,3]=4
tablero[7,4]=1
tablero[7,5]=9
tablero[8,4]=8
tablero[6,6]=2
tablero[6,7]=8
tablero[7,8]=5
tablero[8,7]=7
tablero[8,8]=9

#Mostramos el tablero relleno sin solucionar
print(tablero)

#Empezamos a resolverlo
finalizado=False
while not finalizado:
    contador=0
    #Ciclo anidado para recorrer todo el tablero
    for fila in range(9):
        for columna in range(9):
            #Verificamos donde esten los 0 (esta vacio)
            if tablero[fila,columna]==0:
                #Declaramos todas las opciones posibles
                candidatos=[1,2,3,4,5,6,7,8,9]
                #Verificamos fila y columna
                for i in range(9):
                    #Si una de la fila esta en los candidatos lo sacamos
                    if tablero[i,columna] in candidatos:
                        candidatos.remove(tablero[i,columna])
                    #Si una de la columna esta en los candidatos lo sacamos
                    if tablero[fila,i] in candidatos:
                        candidatos.remove(tablero[fila,i])
                #Verificar subcuadricula:
                sub_cuadricula_fila=fila//3
                sub_cuadricula_columna=columna//3
                #Ciclo anidado para verificar la subcuadricula
                for y in range(sub_cuadricula_fila * 3, (sub_cuadricula_fila + 1) * 3):
                    for x in range(sub_cuadricula_columna * 3, (sub_cuadricula_columna + 1) * 3):
                        #Si uno presente en la subcuadricula esta en candidato lo sacamos
                        if tablero[y,x] in candidatos:
                            candidatos.remove(tablero[y,x])
                #Si queda solo un candidatos lo utilizamos, para cualquier otro caso no podemos estar 100% seguros cual numero va, entonces seguimos
                if len(candidatos)==1:
                    tablero[fila,columna]=candidatos[0]
                    #Si se reemplazo un 0 sumamos al contador
                    contador+=1
    if (tablero.size - np.count_nonzero(tablero))==0:
        finalizado=True
    #Si recorriendo todo el tablero no se pudo cambiar ningun 0 el tablero no se puede resolver
    elif contador==0:
        print("No se puede resolver el tablero de sudoku.")
        break

print(tablero)

#Modulos necesarios para la prueba
import math
import numpy
import time
import random
print(random.random()) #Un float entre 0 y 1
print(random.randint(1,2)) #Un numero entre 1 y 2 incluyendolos (entero)
lista=["Diego", "Eduardo", "Javier"]
print(random.choice(lista)) #Elige un elemento aleatorio de una lista

#En la ayudantía 5 existe más informacion sobre los modulos
#Importante entender el torpedo oficial de la prueba de simulacro, el cual en teoria es el mismo que para la prueba

#Muy importante entender los ciclos anidados, especialmente para recorrer matrices (como se ha trabajado mucho ultimamente)
#Si tienen dudas de la prueba pasada es importante repasarlas, ya que la materia es acumulativa y se utiliza materia pasada para implementar la materia actual