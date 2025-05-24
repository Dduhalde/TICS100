# Ayudantía 10
# Diego Duhalde dduhalde@alumnos.uai.cl

# pip install numpy

import numpy as np # Se importa la librería numpy con el alias np

# Funciones de numpy

# np.array: Crea un array de numpy
# np.arange: Crea un array de numpy con un rango de valores
# np.zeros: Crea un array de numpy con ceros
# np.ones: Crea un array de numpy con unos
# np.sum: Suma los valores de un array
# np.mean: Calcula la media de un array
# np.std: Calcula la desviación estándar de un array
# np.var: Calcula la varianza de un array

# 1D
print(np.array([1, 2, 3, 4, 5])) # Crea un array de numpy con los valores 1, 2, 3, 4, 5
print(np.arange(1, 10)) # Crea un array de numpy con los valores del 1 al 9
print(np.zeros(5)) # Crea un array de numpy con 5 ceros
print(np.sum(np.arange(1, 10))) # Suma los valores del array creado con np.arange
print(np.mean(np.arange(1, 10))) # Suma los valores del array creado con np.arange
print(np.std(np.arange(1, 10))) # Suma los valores del array creado con np.arange

# 2D
print(np.array([[1, 2, 3], [4, 5, 6]])) # Crea una matriz de numpy de 2x3
print(np.arange(1, 13).reshape(3, 4)) # Crea una matriz de numpy de 3x4 con los valores del 1 al 12
print(np.zeros((2, 3))) # Crea una matriz de numpy de 2x3 con ceros
print(np.sum(np.arange(1, 13).reshape(3, 4))) # Suma todos los valores de la matriz 3x4
print(np.mean(np.arange(1, 13).reshape(3, 4))) # Calcula la media de los valores de la matriz 3x4
print(np.std(np.arange(1, 13).reshape(3, 4))) # Calcula la desviación estándar de los valores de la matriz 3x4

# Ejercicio 1
# Dada una matriz NumPy de 3x3 con valores aleatorios entre 0 y 100, normalízala de forma que los valores estén en el rango [0, 1].

# Generar una matriz de 3x3 con valores aleatorios entre 0 y 100
matriz = np.random.randint(0, 100, (3, 3))
print("Matriz original:")
print(matriz)
# Normalizar la matriz
matriz_normalizada = (matriz - np.min(matriz)) / (np.max(matriz) - np.min(matriz))
print("Matriz normalizada:")
print(matriz_normalizada)

# Ejercicio 2
# Dada una matriz de números aleatorios, reemplaza todos los valores menores que 10 por 10 y los mayores que 90 por 90.

# Generar una matriz de 4x4 con valores aleatorios entre 0 y 100
matriz = np.random.randint(0, 100, (4, 4))
print("Matriz original:")
print(matriz)
# Reemplazar valores menores que 10 por 10 y mayores que 90 por 90
matriz[matriz < 10] = 10
matriz[matriz > 90] = 90
print("Matriz modificada:")
print(matriz)

# Ejercicio 3
#Dado un vector v = [1, 2, 3, 4], crea una matriz de 4x4 que tenga ese vector en la diagonal secundaria (de derecha a izquierda).

# Crear un vector
v = np.array([1, 2, 3, 4])
# Crear una matriz de 4x4 con ceros
matriz = np.zeros((4, 4))
# Asignar el vector a la diagonal secundaria
for i in range(len(v)):
    matriz[i, len(v) - 1 - i] = v[i]
print("Matriz con el vector en la diagonal secundaria:")
print(matriz)

# Ejercicio 4
# Dado un arreglo 1D, calcula la media móvil de tamaño 3. Por ejemplo, si el arreglo es [1, 2, 3, 4, 5], el resultado debe ser [2.0, 3.0, 4.0].

# Crear un arreglo 1D
arreglo = np.array([1, 2, 3, 4, 5])
# Calcular la media móvil de tamaño 3

for i in range(len(arreglo) - 2):
    media_movil = np.mean(arreglo[i:i+3])
    print(f"Media móvil de {arreglo[i:i+3]}: {media_movil}")

# Ejercicio 5
# Genera una matriz de 4x4 con números entre 1 y 20. Luego imprime la suma por filas y por columnas por separado.

# Generar una matriz de 4x4 con números aleatorios entre 1 y 20
matriz = np.random.randint(1, 21, (4, 4))
print("Matriz:")
print(matriz)
# Sumar por filas
suma_filas = np.sum(matriz, axis=1)
print("Suma por filas:")
print(suma_filas)
# Sumar por columnas
suma_columnas = np.sum(matriz, axis=0)
print("Suma por columnas:")
print(suma_columnas)

# Ejercicio 6
# Crea una matriz de 6x6 con 1s en el borde y 0s en el centro.

# Crear una matriz de 6x6 con ceros
matriz = np.zeros((6, 6))
# Asignar 1s en el borde
matriz[0, :] = 1
matriz[-1, :] = 1
matriz[:, 0] = 1
matriz[:, -1] = 1
print("Matriz con 1s en el borde y 0s en el centro:")
print(matriz)

# Ejercicio 7
# Extrae la diagonal principal y la diagonal secundaria de una matriz 4x4.

# Crear una matriz de 4x4
matriz = np.random.randint(1, 21, (4, 4))
print("Matriz:")
print(matriz)
# Extraer la diagonal principal
diagonal_principal = np.diag(matriz)
print("Diagonal principal:")
print(diagonal_principal)
# Extraer la diagonal secundaria
diagonal_secundaria = np.diag(np.fliplr(matriz))
print("Diagonal secundaria:")
print(diagonal_secundaria)

