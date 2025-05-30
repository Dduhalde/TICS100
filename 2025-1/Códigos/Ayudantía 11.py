# Ayudantía 11
# Diego Duhalde dduhalde@alumnos.uai.cl

# Estructura
# def nombre_funcion(parametros):
#     cuerpo de la función
#     return valor_de_retorno

# Funciones
def suma(a, b):
    c = a + b
    return c

# Funciones conocidad de Python
print("Hola mundo", end=" ")
print(len("Hola"))
print(type(3.14))
print(abs(-7))
print(max(1, 5, 3))
print(min(1, 5, 3))
print(sum([1, 2, 3]))
print(round(3.14159, 2))
print(sorted([3, 1, 2]))
print(str(123))
print(int("456"))
print(float("7.89"))

# Ejercicio 1
# Crear una funcion que reciba dos números y la operación a realizar, que puede ser suma, resta, multiplicación o división.
def calculadora(num1, num2, operacion):
    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2
    elif operacion == "multiplicación":
        return num1 * num2
    elif operacion == "división":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: División por cero"
    else:
        return "Operación no válida"
    
# Ejemplo de uso
resultado = calculadora(10, 5, "suma")
print(f"Resultado: {resultado}")

# Ejercicio 2
# Utilizando funciones, crear un programa que calcule el área de un círculo, un cuadrado y un triángulo.
import math
def area_circulo(radio):
    return math.pi * radio ** 2
def area_cuadrado(lado):
    return lado ** 2
def area_triangulo(base, altura):
    return (base * altura) / 2

# Ejemplo de uso
radio = 5
lado = 4
base = 3
altura = 6
print(f"Área del círculo: {area_circulo(radio)}")
print(f"Área del cuadrado: {area_cuadrado(lado)}")
print(f"Área del triángulo: {area_triangulo(base, altura)}")

# Ejercicio 3
# Crear una función que reciba una lista de números y retorne la suma de los números pares.
def suma_pares(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            suma += numero
    return suma

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado_pares = suma_pares(numeros)
print(f"Suma de números pares: {resultado_pares}")

# Ejercicio 4
# Crear una función que reciba una cadena de texto y retorne la cantidad de vocales que contiene.
def contar_vocales(cadena):
    contador = 0
    for caracter in cadena.lower():
        if caracter in 'aeiou':
            contador += 1
    return contador
# Ejemplo de uso
texto = "Hola, ¿cómo estás?"
resultado_vocales = contar_vocales(texto)
print(f"Cantidad de vocales en la cadena: {resultado_vocales}")

# Ejercicio 5
# Usando funciones, crear un programa que dos números y retorne si el primero esta contenido en el segundo.
def esta_contenido(num1, num2):
    return str(num1) in str(num2)
# Ejemplo de uso
numero1 = 5
numero2 = 12345
resultado_contenido = esta_contenido(numero1, numero2)
print(f"¿El número {numero1} está contenido en {numero2}? {resultado_contenido}")

# Ejercicio 6
# Crear una función que reciba una lista de palabras y cree una string con las palabras concatenadas, letra por letra. Ejemplo: ["hola", "mundo"] -> "hmoulndao"

def concatenar_letras(lista_palabras):
    resultado = []
    max_length = max(len(palabra) for palabra in lista_palabras)
    
    for i in range(max_length):
        for palabra in lista_palabras:
            if i < len(palabra):
                resultado.append(palabra[i])
    
    return ''.join(resultado)
# Ejemplo de uso
palabras = ["hola", "mundo"]
resultado_concatenado = concatenar_letras(palabras)
print(f"Palabras concatenadas: {resultado_concatenado}")