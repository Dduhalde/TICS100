import time

tiempo_imicial=time.time() #Segundos transcurridos desde el 1 de enero de 1970 hasta el momento de ejecucion
time.sleep(2) #Suspende la ejecucion durante 2 segundos
tiempo_final=time.time()

tiempo_total=tiempo_final-tiempo_imicial #Calcula el tiempo de ejecucion
print(tiempo_total)

tiempo_imicial=time.time()
for i in range(60): #Ciclo desde 0 hasta el 59
    print(i)
    time.sleep(1) #Para cada iteracion se pausa 1 segundo, lo que genera una especie de temporizador de 60 seg
tiempo_final=time.time()
tiempo_total=tiempo_final-tiempo_imicial #Calcula el tiempo de ejecucion del programa y coincide como los 60 segundos del temporizador
print(tiempo_total)

import math

x=10
y=5

print(math.sqrt(x)) #Raiz cuadrada de x
print(math.pow(x, y)) #Potencia x^y
print(math.exp(x)) #Exponencial e^x
print(math.log(x)) #Logaritmo natural de x
print(math.log10(x)) #Logaritmo base 10 de x

#En radianes
print(math.sin(x)) #Seno de x
print(math.cos(x)) #Coseno de x
print(math.tan(x)) #Tangente de x

#Valor de pi
print(math.pi)

#Valor de euler
print(math.e)

import numpy as np

lista=np.array([1,2,3,4]) #Crear lista
matriz=np.array([[1,2],[3,4]]) #Crear matriz

print(np.max(lista)) #Calcula el valor maximo de la lista/matriz
print(np.max(matriz))

print(np.min(lista)) #Calcula el valor minimo de la lista/matriz
print(np.min(matriz))

print(np.mean(lista)) #Calcula el valor promedio de la lista/matriz
print(np.mean(matriz))

print(np.zeros(4)) #Crea lista de ceros con largo 4
print(np.zeros((4,3))) #Crea matriz de ceros con dimension 4x3

print(np.ones(4)) #Crea lista de unos con largo 4
print(np.ones((4,3))) #Crea matriz de unos con dimension 4x3

print(np.full(4,"A")) #Crea lista que contiene "A" con largo 4
print(np.full((4,3),"A")) #Crea matriz que contiene "A" con dimension 4x3

print(np.random.random(4)) #Crea lista con elementos float aleatorios desde 0 al 1 con largo 4
print(np.random.random((4,3))) #Crea matriz con elementos float aleatorios desde 0 al 1 con dimension 4x3

print(np.random.randint(3, size=(4))) #Crea lista con elementos int aleatorios desde 0 al 2 con largo 4
print(np.random.randint(3, size=(4,3))) #Crea matriz con elementos int aleatorios desde 0 al 2 con dimension 4x3

lista=np.append(lista, 5) #Agrega un elemento a la lista que se definio en la linea 42
print(lista)

np.random.shuffle(lista) #Cambia de posicion los elementos de una lista
print(lista)