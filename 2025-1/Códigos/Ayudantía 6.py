# Ayudantía 6
# Diego Duhalde dduhalde@alumnos.uai.cl

# Listas

# Creamos una lista vacia
lista_vacia = []
print(lista_vacia)

# Definimos una lista con elementos
lista = [1, 2, 3, 4, 5]
print(lista)

# Definimos una lista con diferentes tipos de datos
lista = ["Hola", 3, 2.5, [1, 2, 3]]
print(lista)

# Definimos una lista vacia y luego le agregamos elementos
lista = []
lista.append(6)
lista.append(5.5)
print(lista)

# Definimos una lista vacia y luego le agregamos elementos
lista_notas = []
nota_1 = float(input("Ingresa nota 1: "))
nota_2 = float(input("Ingresa nota 2: "))

lista_notas.append(nota_1)
lista_notas.append(nota_2)

print(lista_notas)

import random as rd

# Definimos una lista vacia y luego le agregamos elementos
lista_notas = []
nota_1 = rd.random()*6+1 # rd.uniform(1,7)
nota_2 = rd.random()*6+1

lista_notas.append(round(nota_1,2))
lista_notas.append(round(nota_2,2))

print(lista_notas)

lista = [1,2,3,4,5,3] # Definicion de lista
lista.remove(3)
print(lista)

lista.pop()
print(lista)

lista=[1,2,3,4,5]
print(lista[0])

print(lista[-1])
print(lista[len(lista)-1])

print(lista[0:3])
print(lista[2:])
print(lista[:3])

lista = [1,4,6,3,2,5]
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

lista = [2,5,8,43,6,3]
for i in lista:
    print(i)

for i in range(len(lista)-1):
    #print(lista[i])
    print(i)

# Listas "entrelazadas"
nombres = ["Diego", "Juan", "Matias"]
edades = [23, 21, 29]

for i in range(len(nombres)):
    print(nombres[i], edades[i])


# Ejercicio 1

n = int(input("Ingresa el numero de notas: "))
notas = []

for i in range(n):
    nota = float(input(f"Ingresa la nota {i+1}: "))
    notas.append(nota)

if len(notas) == 0:
    print("No se ingresaron notas")
else:
    print(sum(notas)/len(notas))

# Ejercicio Prueba 1

iteraciones = int(input("Ingrese cantidad de iteraciones: "))
print(f"El programa calculara e con {iteraciones} iteraciones.")

sumatoria = 0
for i in range(1, iteraciones+1, 1):
    #sumatoria = sumatoria + 1/(i**2)
    sumatoria += 1/(i**2)

pi = (sumatoria*6)**(1/2)

print(f"PI calculado con {iteraciones} iteraciones es: {pi}")

# Ejercicio Prueba 2

numeros = []

while True:
    num = int(input("Ingrese un número: "))
    if num <= 0:
        break
    numeros.append(num)

if len(numeros) == 0:
    print("No se ingresaron números positivos.")
else:
    numero_mayor = max(numeros)
    print(f"El número mayor es: {numero_mayor}")

# Ejercicio Prueba 3

edadPacientes = [18, 23, 67, 48, 21, 52]
fumaPacientes = [1, 0, 1, 1, 1, 0]

juventud = []
adultez = []
personaMayor = []

for i in range(len(edadPacientes)):
    if edadPacientes[i] >= 18 and edadPacientes[i] <= 26:
        juventud.append(fumaPacientes[i])
    elif edadPacientes[i] >= 27 and edadPacientes[i] <= 59:
        adultez.append(fumaPacientes[i])
    elif edadPacientes[i] >= 60:
        personaMayor.append(fumaPacientes[i])

print(f"Juventud: {sum(juventud)/len(juventud)*100}%, {sum(juventud)} de los {len(juventud)} jovenes fuman")
print(f"Adultez: {sum(adultez)/len(adultez)*100}%, {sum(adultez)} de los {len(adultez)} adultos fuman")
print(f"Persona Mayor: {sum(personaMayor)/len(personaMayor)*100}%, {sum(personaMayor)} de los {len(personaMayor)} adultos mayores fuman")