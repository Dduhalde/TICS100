# Ayudantía 5
# Diego Duhalde dduhalde@alumnos.uai.cl

# Ciclos
# while
# for

# Ciclo while requiere una condición que se evalúa como True o False
# El ciclo se ejecuta mientras la condición sea True
# Se puede usar un break para salir del ciclo
# Se puede usar un continue para saltar a la siguiente iteración del ciclo

# Ciclo for no utiliza una condición, sino que itera una cantidad fija de veces
# Se puede usar un break para salir del ciclo
# Se puede usar un continue para saltar a la siguiente iteración del ciclo
# range() genera una secuencia de números enteros
# range(inicio, fin, paso) genera una secuencia de números enteros desde inicio hasta fin-1 con un paso de paso

print(list(range(0,10,1))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(0,10,2))) # [0, 2, 4, 6, 8]
print(list(range(10,0,-1))) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

condicion = True # Inicializa la condición

while condicion:
    print("Ejemplo de while")
    condicion = False # Cambia la condición para salir del ciclo

for i in range(10):
    print("Ejemplo de for", i)
    # El ciclo for se ejecuta 10 veces, desde 0 hasta 9

# Ejercicio 1.1 Imprime los números del 1 al 10.

for i in range(1, 11):
    print(i)

inicio = 1
while inicio <= 10:
    print(inicio)
    inicio += 1 # Incrementa el valor de inicio en 1

# Se puede hacer con while o for, pero es más fácil con for

# Ejercicio 1.2 Pide un número al usuario e imprime su tabla (de multiplicar) del 1 al 10.

num = int(input("Ingrese un número: "))
for i in range(1, 11):
    print(num, "*", i, "=", num * i)

# Ejercicio 1.3 Suma los números desde 1 hasta n (sumatoria).

n = int(input("Ingrese un número: "))
suma = 0
for i in range(1, n + 1):
    suma += i # suma = suma + i
print(f"La suma de los números desde 1 hasta {n} es {suma}")

# Ejercicio 2.1 Adivina un número del 1 al 5, con una cantidad de 3 intentos máximos.
import random as rd

intentos = 3
numero = rd.randint(1, 5) # Genera un número aleatorio entre 1 y 5

print("Adivina el número del 1 al 5")
print("Tienes 3 intentos")
while intentos > 0:
    intento = int(input("Ingrese su intento: "))
    if intento == numero:
        print("¡Adivinaste!")
        break # Sale del ciclo
    else:
        intentos -= 1 # Decrementa el número de intentos
        print("Fallaste, te quedan", intentos, "intentos")

# Ejericicio 2.2 Haz un temporizador de 10 segundos
import time

for i in range(10, 0, -1):
    print(i)
    time.sleep(1) # Espera 1 segundo
print("¡Tiempo terminado!")

# Ejercicio 2.3 Simula un login, solicitando user y password, se tienen máximo 5 intentos para ingresar.
# Si se ingresa el user y password correcto, se imprime "Bienvenido" y se sale del ciclo.
# Si se ingresa el user y password incorrecto, se imprime "Usuario o contraseña incorrectos" y se decrementa el número de intentos.
# Si se llega a 0 intentos, se imprime "Se han agotado los intentos".

user = "admin"
password = "1234"
intentos = 5

print("Bienvenido al sistema")
print("Tienes 5 intentos para ingresar")

while intentos > 0:
    user_input = input("Ingrese su usuario: ")
    password_input = input("Ingrese su contraseña: ")
    if user_input == user and password_input == password:
        print("Bienvenido")
        break # Sale del ciclo
    else:
        intentos -= 1 # Decrementa el número de intentos
        print("Usuario o contraseña incorrectos, te quedan", intentos, "intentos")
if intentos == 0:
    print("Se han agotado los intentos")

# Ejercicio 3.1 Pide un número al usuario y verifica si el número es primo o no.
# Un número primo es un número mayor que 1 que solo es divisible por 1 y por sí mismo.
# Por ejemplo, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 son números primos.

# Un número no primo es un número que tiene más de dos divisores.
# Por ejemplo, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18 son números no primos.
# 0 y 1 no son números primos.
# 0 es divisible por todos los números y 1 solo es divisible por sí mismo.
# Por lo tanto, no son números primos.
# Un número negativo no es primo.

numero = int(input("Ingrese un número: "))

if numero < 2:
    print(f"{numero} no es primo")
else:
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"{numero} es primo")
    else:
        print(f"{numero} no es primo")
