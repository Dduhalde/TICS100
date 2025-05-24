# Ayudantía 7
# Diego Duhalde dduhalde@alumnos.uai.cl

# Corrección Prueba 1

# Pregunta 1
# Hacer un programa que pida al usuario n cantidad de precios y luego calcule el valor neto y el IVA del total.
# El IVA es el 19% del total. El valor neto es el total menos el IVA.

# Verision 1 con lista
n = int(input("Ingrese la cantidad de precios: "))
lista_precios = []

for i in range(1, n+1):
    precio = int(input(f"Ingrese el precio N°{i}: "))
    lista_precios.append(precio)

iva_total = sum(lista_precios) * 0.19
valor_neto_total = sum(lista_precios) - iva_total

print(f"El IVA total es: {iva_total}")
print(f"El valor neto total es: {valor_neto_total}")

# Verision 2 sin lista
n = int(input("Ingrese la cantidad de precios: "))
suma_precios = 0

for i in range(1, n+1):
    precio = int(input(f"Ingrese el precio N°{i}: "))
    suma_precios += precio # suma_precios = suma_precios + precio

iva_total = suma_precios * 0.19
valor_neto_total = suma_precios - iva_total

print(f"El IVA total es: {iva_total}")
print(f"El valor neto total es: {valor_neto_total}")

# Pregunta 2
# Se tiene el siguiente código para verificar si un número es primo o no.

numeroPrimo = int(input("Ingrese un número: "))
esPrimo = False
i = 1

while i < numeroPrimo:
    esPrimo = numeroPrimo%i == 0
    i = i +1

if esPrimo:
    print("El número es primo")
else:
    print("El número no es primo")

# Verifique el codigo para numeroPrimo = 1 y numeroPrimo = 4. ¿Es correcto? Justifique su respuesta.
# Arregle el código para que funcione correctamente.

# Version 1 con break
numeroPrimo = int(input("Ingrese un número: "))
esDivisible = False
i = 2

while i < numeroPrimo:
    esDivisible = numeroPrimo%i == 0
    if esDivisible == True:
        break
    i = i +1

if esDivisible:
    print("El número no es primo")
else:
    print("El número es primo")

# Version 2 sin break

numeroPrimo = int(input("Ingrese un número: "))
esDivisible = False
i = 2

while i < numeroPrimo and esDivisible == False:
    esDivisible = numeroPrimo%i == 0
    i = i +1

if esDivisible:
    print("El número no es primo")
else:
    print("El número es primo")

# Pregunta 3
# Se tiene una lista de alfabeto, la cual contiene las letras del alfabeto en orden y como ultimo elemento el espacio. (No contiene la ñ)
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' '] # 27 elementos
# Se tiene una lista que contiene una palabra encriptada, la cual es una lista de enteros. Cada entero representa la posición de la letra en el alfabeto. Por ejemplo, si la palabra es "hola", la lista sera [7, 14, 11, 0].
# Si la lista contiene un número mayor a 27 se debe parar de decodificar y se debe imprimir la palabra decodificada hasta ese momento.
mensaje = [7, 14, 11, 0, 7, 3, 4] # [h, o, l, a]
# Se debe imprimir la palabra decodificada. Por ejemplo, si la lista es [7, 14, 11, 0], se debe imprimir "hola".

# Version 1 con break
for letra_encriptada in mensaje:
    if letra_encriptada >= 27:
        break
    print(alfabeto[letra_encriptada], end='') # end='' para que no salte de linea"""

# Version 2 sin break
i = 0
while i < len(mensaje) and mensaje[i]<=27:
    print(alfabeto[mensaje[i]], end='')
    i += 1