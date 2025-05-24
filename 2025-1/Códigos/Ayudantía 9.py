# Ayudantía 9
# Diego Duhalde dduhalde@alumnos.uai.cl

# Un ciclo anidado es un ciclo dentro de otro ciclo. El ciclo interno se ejecuta completamente cada vez que el ciclo externo da una vuelta.

# Ejemplos de ciclos anidados

# Ejemplo 1
for i in range(5):
    for j in range(5):
        print(i, j)
    print("Fin del ciclo interno")
print("Fin del ciclo externo")

# Ejemplo 2
lista = ["Diego", "Juan", "Pedro"]
for i in range(len(lista)):
    for j in range(len(lista)):
        print(f"{lista[i]} {lista[j]}")
    print("Fin del ciclo interno")
print("Fin del ciclo externo")

# Ejemplo 3
for i in range(5):
    for j in range(5):
        print(i, j)
        if i == 2 and j == 2:
            break
    print("Fin del ciclo interno")
print("Fin del ciclo externo")

# Ejercicio 1
# Viendo como funciona el ciclo anidado, hacer un programa que imprima una tabla de multiplicar del 1 al 10.

# Solución
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print("Fin de la tabla de multiplicar del", i)

# Ejercicio 2.1
# Apoyandose del ejemplo, muestre un tablero de ajedrez de 8x8, donde las casillas blancas son espacios y las negras son "X"

# Solución

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print(" ", end=" ")
        else:
            print("X", end=" ")
    print()  # Salto de línea al final de cada fila

# Ejercicio 2.2
# Ahora escriba las coordenadas de cada casilla, por ejemplo, A1, B2, C3, D4, E5, F6, G7, H8

# Solución
columnas = "ABCDEFGH"
for i in range(8):
    for j in range(8):
        print(f"{columnas[j]}{i + 1}", end=" ")
    print()  # Salto de línea al final de cada fila

# Ejercicio 3
# Escriba un programa que imprima el siguiente patrón:
# 1
# 12
# 123
# 1234
# 12345
# 123456

# Solución
for i in range(1, 7):
    for j in range(1, i + 1):
        print(j, end="")
    print()  # Salto de línea al final de cada fila

# Ejercicio 4
# Dibuje un triángulo de asteriscos en consola

# Solución
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()  # Salto de línea al final de cada fila

# Ejercicio 5
# Muestre un cuadro 5x5 donde la diagonal principal sea un asterisco y el resto espacios
# Solución
for i in range(5):
    for j in range(5):
        if i == j:
            print("*", end="")
        else:
            print(" ", end="")
    print()  # Salto de línea al final de cada fila

# Ejercicio 6
# Muestre un cuadro 5x5 donde los bordes sean asteriscos y el resto espacios
# Solución
for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()  # Salto de línea al final de cada fila