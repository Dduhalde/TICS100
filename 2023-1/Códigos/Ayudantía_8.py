import random as rd
import numpy as np
# Funciones
def funcion(argumento1, argumento2):
    return

def saludos():
    return "Hola! Que tengas un excelente día."

print(saludos())
saludo=saludos()

def funcion_matematica(x, y):
    operacion = x * y
    operacion = operacion + (2*x) - y
    operacion = operacion*operacion
    return operacion

print(funcion_matematica(3, 4))

def funcion_matematica2():
    x = rd.randint(1,9)
    y = rd.randint(1,9)
    operacion = x * y
    operacion = operacion + (2*x) - y
    operacion = operacion*operacion
    return operacion

print(funcion_matematica2())

def saludos_nombre(nombre):
    return f"Hola {nombre}! Que tengas un excelente día."

print(saludos_nombre("Diego"))

nombres = ["Diego", "Sebastian", "Matias"]
for nombre in nombres:
    print(saludos_nombre(nombre))

# Programa que verifique si un numero es primo, si lo es calcule su factorial
def num_primo(num):
    for i in range(2, num):
        if num%i==0:
            return f"El numero {num} no es primo."
    return factorial(num)

def factorial(num):
    fact=1
    for i in range(2, num+1):
        fact = fact*i
    return f"El factorial del numero {num} es: {fact}"

print(num_primo(6))
print(num_primo(7))
print(num_primo(124))
print(num_primo(123))

# Producto de todos los digitos de un numero
def producto_digitos(num):
    multiplicacion = 1
    for i in str(num):
        multiplicacion = multiplicacion*int(i)
    return multiplicacion

print(producto_digitos(65462))

# Mostrar todos los numeros impares hasta n numero
def num_impares(num):
    for i in range(1,num+1,2):
        print(i)
    return

num_impares(13)

# Agregar todos los numeros impares hasta n numero en una lista
def num_impares_lista(num):
    lista=[]
    for i in range(1,num+1,2):
        lista.append(i)
    return lista

print(num_impares_lista(20))

# Verificar si un correo es valido
# Que contenga @ y .
def verificar_correo(correo):
    return "@" in correo and "." in correo

print(verificar_correo("dduhalde@alumnos.uai.cl"))

# Programa que calcule el promedio de x notas
def promedio(num_notas):
    notas=[]
    for i in range(num_notas):
        nota=float(input(f"Ingrese la nota {i+1}: "))
        notas.append(nota)
    promedio = round(np.mean(notas),1)
    return f"El promedio de las {num_notas} notas es de {promedio}."

def promedio_alumnos(num_alumnos):
    for i in range(num_alumnos):
        num_notas=int(input(f"Ingrese cuantas notas tiene el alumno {i+1}: "))
        print(promedio(num_notas))
    return

promedio_alumnos(2)