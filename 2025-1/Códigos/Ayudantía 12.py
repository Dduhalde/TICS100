# Ayudantía 12
# Diego Duhalde dduhalde@alumnos.uai.cl

# Ejercicio 1, Pesos de usuarios (NumPy)

import numpy as np

numUsuarios = int(input("Ingrese la cantidad de usuarios: "))
pesos = np.zeros(numUsuarios)

for i in range(numUsuarios):
    peso = float(input(f"Ingrese el peso del usuario {i+1} (kg): "))
    pesos[i] = peso

print(f"Peso mínimo: {np.min(pesos)} kg")
print(f"Peso promedio: {np.mean(pesos)} kg")
print(f"Peso máximo: {np.max(pesos)} kg")

# Ejercicio 2, Depuración de letra T

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

# Codigo con errores
for i in range(filas):  
    for j in range(columnas):  
        if i == 0 or j == columnas//2:  
            print("*", end="")

# Corrección del código
for i in range(filas):
    for j in range(columnas):
        if i == 0:
            print("*", end="")
        elif j == columnas // 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Ejercicio 3, Pozos térmicos

import numpy as np

def detectarPozos(matriz):
    matriz = np.array(matriz)
    filas, columnas = matriz.shape
    pozos = 0
    temperaturaMinima = None

    for i in range(1, filas-1):
        for j in range(1, columnas-1):
            valor = matriz[i, j]
            vecinos = matriz[i-1:i+2, j-1:j+2].flatten()
            vecinosSinCentro = np.delete(vecinos, 4)
            if np.all(valor < vecinosSinCentro):
                pozos += 1
                if temperaturaMinima is None or valor < temperaturaMinima:
                    temperaturaMinima = valor

    print(f"La temperatura más baja en un pozo es {temperaturaMinima}°C.")
    return pozos

# Ejemplo de uso:
temperaturas = [
    [22, 25, 20, 21, 24],
    [26, 19, 22, 18, 23],
    [27, 21, 17, 20, 26],
    [28, 22, 19, 22, 24],
    [29, 25, 23, 24, 22]
]

resultado = detectarPozos(temperaturas)
print(f"Cantidad de pozos térmicos: {resultado}")