# Ayudantía 4
# Diego Duhalde dduhalde@alumnos.uai.cl

# Condicionales
# If, elif, else
# Operadores lógicos: and, or, not
# Operadores de comparación: ==, !=, <, <=, >, >=

# Ejemplo uso if
if True:
    print("Es verdadero")
else:
    print("Es falso")

# Ejemplo uso if con comparación
if 5 > 3:
    print("5 es mayor que 3")
else:
    print("5 no es mayor que 3")

# Ejemplo uso if con comparación y operador lógico
if 5 > 3 and 3 < 5:
    print("5 es mayor que 3 y 3 es menor que 5")
else:
    print("No se cumple la condición")

# Ejemplo uso if con comparación y operador lógico
if 5 > 3 or 3 > 5:
    print("Al menos una de las condiciones es verdadera")
else:
    print("Ambas condiciones son falsas")

# Ejercicio 1.1 Pide un número al usuario y muestra si es positivo, negativo o cero.

numero = float(input("Ingrese un número: "))

if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")

# Ejercicio 1.2 Verifica si un número ingresado es par o impar.

numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# Ejercicio 1.3 Pide dos números y muestra cuál es mayor, o si son iguales.

numero_1 = float(input("Ingrese el primer número: "))
numero_2 = float(input("Ingrese el segundo número: "))

if numero_1 > numero_2:
    print("El primer número es mayor")
elif numero_1 < numero_2:
    print("El segundo número es mayor")
else:
    print("Los números son iguales")

# Ejercicio 2.1 Pide la edad del usuario y clasifícalo en: niño (0-12), adolescente (13-17), adulto (18-64), adulto mayor (65+).

edad = int(input("Ingrese su edad: "))

if edad < 0:
    print("Edad inválida")
elif edad <= 12:
    print("Eres un niño")
elif edad <= 17:
    print("Eres un adolescente")
elif edad <= 64:
    print("Eres un adulto")
elif edad >= 65:
    print("Eres un adulto mayor")
else:
    print("Edad inválida")

# Ejercicio 2.2 Pide una nota entre 1 y 7 y entrega una calificación textual:
#1.0 a 3.9 → "Reprobado"
#4.0 a 5.4 → "Aprobado"
#5.5 a 6.4 → "Bueno"
#6.5 a 7.0 → "Excelente"

nota = float(input("Ingrese su nota (1.0 a 7.0): "))

if nota < 1.0 or nota > 7.0:
    print("Nota inválida")
elif nota < 4.0:
    print("Reprobado")
elif nota < 5.5:
    print("Aprobado")
elif nota < 6.5:
    print("Bueno")
elif nota <= 7.0:
    print("Excelente")
else:
    print("Nota inválida")

# Ejercicio 3.1 Pide peso y altura, calcula el IMC y clasifica:
#< 18.5 → Bajo peso
#18.5–24.9 → Normal
#25–29.9 → Sobrepeso
#30+ → Obesidad

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print("Bajo peso")
elif imc < 25:
    print("Normal")
elif imc < 30:
    print("Sobrepeso")
elif imc >= 30:
    print("Obesidad")
else:
    print("IMC inválido")
