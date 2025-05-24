#dduhalde@alumnos.uai.cl

#Ciclos for

#for i in range(inicio, final-1, paso):
#por default inicio es 0 y paso es 1

#Ejemplos Básicos

for i in range(2, 10, 2):
    print(i)

for i in range(30, 2, -1):
    print(i)

variable="DIEGO"

for i in variable:
    print(i)

#Ejercicio N°1: calcular promedio de n notas.

numero_notas=int(input("Cantidad de notas para calcular el promedio: "))
suma_notas=0

for i in range(1, numero_notas+1, 1):
    nota=float(input(f"Ingrese la nota N°{i}: "))
    suma_notas=suma_notas+nota
promedio=suma_notas/numero_notas

print(f"El promedio es: {round(promedio,2)}")

#Ejercicio N°2: divisores de un numero.

numero=int(input("Ingrese un numero: "))
contador=0
for i in range(1, numero+1):
    if numero%i==0:
        print(f"El numero {i} es divisor de {numero}.")
        contador=contador+1

print(f"El numero {numero} tiene {contador} divisores.")

#Ejercicio N°3: Verificar si un numero es primo.

#Forma 1
numero=int(input("Ingrese un numero: "))
contador=0

for i in range(1, numero+1):
    if numero%i==0:
        contador=contador+1

if contador==2:
    print(f"El numero {numero} es primo.")
else:
    print(f"El numero {numero} no es primo.")

#Forma 2
numero=int(input("Ingrese un numero: "))
es_primo=True
for i in range(2, numero):
    if numero%i==0:
        print(f"El numero {numero} no es primo.")
        es_primo=False
        break
if es_primo:
    print(f"El numero {numero} es primo.")

#Ejercicio N°4: Mostrar todos los numeros impares hasta n numero.

numero=int(input("Ingrese un numero: "))
for i in range(1, numero+1, 2):
    print(i)

#Ejercicio N°5: Contar cuantas veces aparece una letra en una frase.

letra=input("Ingrese una letra: ")
frase=input("Ingrese una frase: ")

contador=0
for letra_en_frase in frase:
    if letra==letra_en_frase:
        contador=contador+1

print(f"La letra {letra} aparece {contador} veces en nuestra frase.")

#Ejercicio N°6: Calcular el factorial de un numero:

numero=int(input("Ingrese un numero: "))
factorial=1

for num in range(2, numero+1):
    factorial=factorial*num

print(f"El factorial de {numero} es: {factorial}")

#Ejercicio N°7: Ejemplo sumatoria:

sumatoria=0
for i in range(1, 5):
    sumatoria=sumatoria+((3*i)-1)

print(f"El resultado de la sumatoria es: {sumatoria}")

#Ejercicio N°8: Ejemplo productoria:

productoria=0
for i in range(1, 5):
    productoria=productoria+((3*i)-1)

print(f"El resultado de la productoria es: {productoria}")