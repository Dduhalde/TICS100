#dduhalde@alumnos.uai.cl

#Tipos de variable en python

#String-str
#Integers-int
#Floating-float

string="hola"
int=10
float=10.0

#Formas de print en python

Edad=20

print(string)
print("Tu edad es", Edad)
print(f"Tu edad es {Edad}")
print(f"Hola")

#Input en python (consultas en terminal)

Respuesta = input()
Respuesta2 = str(input("¿Cual es tu color favorito? "))
Respuesta3 = int(input("¿Cual es tu edad? "))

Precio = str(input("Ingresa el precio del producto: "))
print(Precio*1.19)

#Operadores en python

Numero=10
Numero2=20

print(f"La suma es: {Numero+Numero2}")
print(f"La resta es: {Numero-Numero2}")
print(f"La multiplicacion es: {Numero*Numero2}")
print(f"La division es: {Numero/Numero2}")
print(f"La exponencial es: {Numero**Numero2}")
print(f"La raiz cuadrada es: {Numero**(1/2)}")
print(f"La resto es: {Numero%Numero2}")
print(f"La parte entera de la division es: {Numero//Numero2}")

#Condicionales

#if
#elif
#else

Edad=15

if Edad>=18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

Color="Rojo"

if Color=="Rojo":
    print("Te gusta el rojo")
elif Color=="Azul":
    print("Te gusta el azul")
else:
    print("Te gusta el amarillo")

Numero=1

if Numero==1:
    print("Te gusta el rojo")
elif Numero==1:
    print("Te gusta el azul")
else:
    print("Te gusta el amarillo")

if Numero==1:
    print("Te gusta el rojo")
if Numero==1:
    print("Te gusta el azul")
if Numero==1:
    print("Te gusta el amarillo")

#Ejercicio 1

"""Ejercicio: Calculadora de precios
Escribe un programa que calcule el precio de un producto en función de su categoría y el país de origen. El programa deberá hacer lo siguiente:

Pedir al usuario que ingrese el precio base del producto.
Pedir al usuario que indique la categoría del producto (A, B o C).
Pedir al usuario que indique el país de origen del producto (EE.UU., México o Canadá).
Calcular el precio final del producto en función de su categoría y país de origen según las siguientes reglas:
Si la categoría del producto es A y el país de origen es EE.UU., el precio final será el precio base multiplicado por 1.1.
Si la categoría del producto es A y el país de origen es México, el precio final será el precio base multiplicado por 1.15.
Si la categoría del producto es A y el país de origen es Canadá, el precio final será el precio base multiplicado por 1.05.
Si la categoría del producto es B y el país de origen es EE.UU., el precio final será el precio base multiplicado por 1.12.
Si la categoría del producto es B y el país de origen es México, el precio final será el precio base multiplicado por 1.18.
Si la categoría del producto es B y el país de origen es Canadá, el precio final será el precio base multiplicado por 1.07.
Si la categoría del producto es C y el país de origen es EE.UU., el precio final será el precio base multiplicado por 1.08.
Si la categoría del producto es C y el país de origen es México, el precio final será el precio base multiplicado por 1.12.
Si la categoría del producto es C y el país de origen es Canadá, el precio final será el precio base multiplicado por 1.03.
Mostrar el precio final del producto con dos decimales."""

Precio=int(input("Ingrese el precio base del producto: "))
Categoria=input("Indique la categoría del producto (A, B o C): ")
Pais=input("Indique el país de origen del producto (EE.UU., México o Canadá): ")

if Categoria=="A":
    if Pais=="EE.UU.":
        multiplicador=1.1
    elif Pais=="México":
        multiplicador=1.15
    else:
        multiplicador=1.05
elif Categoria=="B":
    if Pais=="EE.UU.":
        multiplicador=1.12
    elif Pais=="México":
        multiplicador=1.18
    else:
        multiplicador=1.07
else:
    if Pais=="EE.UU.":
        multiplicador=1.08
    elif Pais=="México":
        multiplicador=1.12
    else:
        multiplicador=1.03

print(f"El precio final es {round(Precio*multiplicador,2)}")

#Ejercicio 2

"""Ejercicio: Ordenar tres números
Escribe un programa que pida al usuario que ingrese tres números enteros y los muestre en orden ascendente. El programa deberá hacer lo siguiente:

Pedir al usuario que ingrese el primer número.
Pedir al usuario que ingrese el segundo número.
Pedir al usuario que ingrese el tercer número.
Verificar cuál es el número más pequeño y cuál es el número más grande utilizando condicionales anidados.
Imprimir los números en orden ascendente."""

Num1=int(input("Ingrese el primer número: "))
Num2=int(input("Ingrese el segundo número: "))
Num3=int(input("Ingrese el tercero número: "))

if Num1<=Num2:
    if Num1<=Num3:
        print(Num1)
        if Num2<=Num3:
            print(Num2)
            print(Num3)
        else: #Num3<Num2
            print(Num3)
            print(Num2)
    else:
        print(Num3)
        print(Num1)
        print(Num2)
else: #Num2<Num1
    if Num2<=Num3:
        print(Num2)
        if Num1<=Num3:
            print(Num1)
            print(Num3)
        else: #Num3<Num1
            print(Num3)
            print(Num1)
    else:
        print(Num3)
        print(Num2)
        print(Num1)
