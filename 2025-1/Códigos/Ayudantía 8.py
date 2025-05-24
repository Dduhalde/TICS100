# Ayudantía 8
# Diego Duhalde dduhalde@alumnos.uai.cl

# Repaso Ciclos

# Ciclo for
# for i in range(start, stop, step): # ciclo para en stop-1
#   print(i)
# for elemento in lista:
#   print(elemento)
# for letra in string:
#   print(letra)

for i in range(10): # Start por defecto es 0, step por defecto es 1
    print(i)

for i in range(1, 10): # Step por defecto es 1
    print(i)

for i in range(1, 10, 2): # Todos los argumentos definidos
    print(i)

palabra = "Hola"
for letra in palabra:
    print(letra)

notas = [6.5, 7.0, 5.5, 4.0]
for nota in notas:
    print(nota)

# Ciclo while
# while condicion:
#   hacer algo
#   editar condicion

# SI O SI HAY QUE CAMBIAR LA CONDICION O USAR BREAK, O SINO SE HACE UN CICLO INFINITO

# Condicion ocupa ==, !=, <, >, <=, >=, and, or, not, in
# Ejemplo de ciclo while
i = 0
while i < 10:
    print(i)
    i += 1 # i = i + 1

# Ejemplo de ciclo while con break
i = 0
while True: # Ciclo infinito
    print(i)
    i += 1
    if i == 10:
        break # Sale del ciclo

# Ejercicio 1
# Escribir un programa que pida al usuario un número entero positivo y calcule la suma de todos los números enteros desde 1 hasta ese número.
# Ejemplo: si el usuario ingresa 5, la salida debe ser 15 (1+2+3+4+5)

# Solución

# Solución for
numero = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(1, numero + 1):
    suma += i
print("La suma de los números enteros desde 1 hasta", numero, "es:", suma)

# Solución while
numero = int(input("Ingrese un número entero positivo: "))
suma = 0
i = 1
while i <= numero:
    suma += i
    i += 1
print("La suma de los números enteros desde 1 hasta", numero, "es:", suma)

# Ejercicio 2
# Escribir un programa que pida al usuario un número entero positivo y calcule el factorial de ese número.
# Ejemplo: si el usuario ingresa 5, la salida debe ser 120 (1*2*3*4*5)

# Solución

# Solución for
numero = int(input("Ingrese un número entero positivo: "))
factorial = 1
for i in range(1, numero + 1):
    factorial *= i
print("El factorial de", numero, "es:", factorial)

# Solución while
numero = int(input("Ingrese un número entero positivo: "))
factorial = 1
i = 1
while i <= numero:
    factorial *= i
    i += 1
print("El factorial de", numero, "es:", factorial)

# Ejercicio 3
# Escribir un programa que pida al usuario un número entero positivo y calcule la suma de los dígitos de ese número.
# Ejemplo: si el usuario ingresa 123, la salida debe ser 6 (1+2+3)

# Solución

# Solución for
numero = int(input("Ingrese un número entero positivo: "))
suma = 0
for digito in str(numero):
    suma += int(digito)
print("La suma de los dígitos de", numero, "es:", suma)

# Ejercicio 4
# Usando un ciclo while, hacer un menu de opciones para que el usuario pueda elegir entre las siguientes opciones:
# 1. Sumar dos números
# 2. Restar dos números
# 3. Multiplicar dos números
# 4. Dividir dos números
# 5. Salir
# El programa debe seguir mostrando el menú hasta que el usuario elija la opción 5.

# Solución

while True:
    print("Menu de opciones:")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Salir")
    opcion = int(input("Ingrese su opción: "))
    if opcion == 1:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 + num2
        print("La suma es:", resultado)
    elif opcion == 2:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 - num2
        print("La resta es:", resultado)
    elif opcion == 3:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 * num2
        print("La multiplicación es:", resultado)
    elif opcion == 4:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        if num2 != 0:
            resultado = num1 / num2
            print("La división es:", resultado)
        else:
            print("Error: División por cero.")
    elif opcion == 5:
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intente nuevamente.")

# Ciclos anidados (Los veran el jueves con más detalle)

for i in range(5):
    for j in range(5):
        print(i, j)
    print("Fin del ciclo interno")
print("Fin del ciclo externo")

# Ejercicio 5
# Viendo como funciona el ciclo anidado, hacer un programa que imprima una tabla de multiplicar del 1 al 10.

# Solución
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print("Fin de la tabla de multiplicar del", i)

# Ejercicio 6.1
# Apoyandose del ejemplo, muestre un tablero de ajedrez de 8x8, donde las casillas blancas son espacios y las negras son "X"

# Solución

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print(" ", end=" ")
        else:
            print("X", end=" ")
    print()  # Salto de línea al final de cada fila

# Ejercicio 6.2
# Ahora escriba las coordenadas de cada casilla, por ejemplo, A1, B2, C3, D4, E5, F6, G7, H8

# Solución
columnas = "ABCDEFGH"
for i in range(8):
    for j in range(8):
        print(f"{columnas[j]}{i + 1}", end=" ")
    print()  # Salto de línea al final de cada fila