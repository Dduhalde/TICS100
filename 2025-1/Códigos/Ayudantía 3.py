# Ayudantía 3
# Diego Duhalde dduhalde@alumnos.uai.cl

# Funciones
print("Función Print", sep=" ", end="\n", ) # Tres argumentos: texto, separador y fin

# Módulos
import math # Módulo matemático
import random # Módulo aleatorio
import time # Módulo de tiempo

# Se pueden abreviar módulos
import math as mt # Abreviación del módulo matemático
import random as rd # Abreviación del módulo aleatorio
import time as tm # Abreviación del módulo de tiempo

# Funciones de módulos Math
print(mt.pi) # Número pi
print(mt.e) # Número e
print(mt.sqrt(16)) # Raíz cuadrada de 16
print(mt.factorial(5)) # Factorial de 5
print(mt.pow(2, 3)) # Potencia de 2 elevado a 3
print(mt.sin(0)) # Seno de 0 radianes
print(mt.cos(0)) # Coseno de 0 radianes
print(mt.tan(0)) # Tangente de 0 radianes
print(mt.log(10)) # Logaritmo natural de 10
print(mt.log10(10)) # Logaritmo base 10 de 10
print(mt.degrees(1)) # Radianes a grados
print(mt.radians(180)) # Grados a radianes
print(mt.ceil(3.2)) # Redondeo hacia arriba
print(mt.floor(3.2)) # Redondeo hacia abajo
print(mt.trunc(3.2)) # Truncamiento
print(mt.fabs(-3.2)) # Valor absoluto
print(mt.factorial(5)) # Factorial de 5

# Funciones de módulos Random
print(rd.random()) # Número aleatorio entre 0 y 1
print(rd.randint(1, 10)) # Número aleatorio entre 1 y 10
print(rd.uniform(1, 10)) # Número aleatorio entre 1 y 10 con decimales
print(rd.choice([1, 2, 3, 4, 5])) # Elección aleatoria de una lista
print(rd.sample([1, 2, 3, 4, 5], 3)) # Muestra aleatoria de una lista

# Funciones de módulos Time
print(tm.time()) # Tiempo actual en segundos desde el epoch
print(tm.localtime()) # Tiempo local
print(tm.gmtime()) # Tiempo GMT

# Ejercicio 1
# Generar 5 números aleatorios entre 1 y 100, calcula su raíz cuadrada y mide el tiempo que toma la operación.
# Imprime el resultado y el tiempo de ejecución.
import random as rd
import time as tm
import math as mt

# Generar 5 números aleatorios entre 1 y 100
num_1 = rd.randint(1, 100)
num_2 = rd.randint(1, 100)
num_3 = rd.randint(1, 100)
num_4 = rd.randint(1, 100)
num_5 = rd.randint(1, 100)

print("Números aleatorios:", num_1, num_2, num_3, num_4, num_5)

# Calcular la raíz cuadrada de cada número y medir el tiempo de ejecución
start_time = tm.time()
sqrt_1 = mt.sqrt(num_1)
sqrt_2 = mt.sqrt(num_2)
sqrt_3 = mt.sqrt(num_3)
sqrt_4 = mt.sqrt(num_4)
sqrt_5 = mt.sqrt(num_5)
end_time = tm.time()
execution_time = end_time - start_time

print("Raíces cuadradas:", sqrt_1, sqrt_2, sqrt_3, sqrt_4, sqrt_5)
print("Tiempo de ejecución:", execution_time, "segundos")

# Ejercicio 2
#  Pide un número al usuario y aplica 3 funciones del módulo de math.
# Imprime el resultado de cada función y el tiempo que toma cada operación.

import time as tm
import math as mt

num = float(input("Ingrese un número: "))
print(f"Número ingresado: {num}")

start_time = tm.time()

print(f"Raíz cuadrada de {num}: {mt.sqrt(num)}")
print(f"Factorial de {num}: {mt.factorial(int(num))}")
print(f"Cubo de {num}: {mt.pow(num, 3)}")

end_time = tm.time()
execution_time = end_time - start_time

print(f"Tiempo de ejecución: {execution_time} segundos")