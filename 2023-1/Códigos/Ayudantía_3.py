#dduhalde@alumnos.uai.cl

#Ciclos While

#Ciclo que funciona hasta que una o más condiciones se dejan de cumplir

x=5
while x!=0:
    x=x-1
    print("Hola")

x=0
while x!=5:
    x=x+1
    print("Chao")

x=6
y=7

while x>=0 or y>=0:
    x=x-1
    print("Hola")

while x>=0 and y>=0:
    x=x-1
    print("Hola")

x="NO"

while x!="Salir":
    x=input("¿Salir?: ")

#1. Programa que sume n numeros hasta que el usuario responda si:

respuesta=0
suma=0

while respuesta!="SI":
    numero=int(input("Ingrese un numero: "))
    suma=suma+numero
    respuesta=input("Desea salir del programa? (SI/NO): ")

print(f"La suma final es {suma}")

#2. Programa para iniciar sesion, con maximo 5 intentos incorrectos

usuario="dduhalde"
contraseña="1234"
intentos=5
usuario_ingresado=""
contraseña_ingresada=""

while (usuario!=usuario_ingresado or contraseña!=contraseña_ingresada) and intentos!=0:
    usuario_ingresado=input("Ingrese su usuario: ")
    contraseña_ingresada=input("Ingrese su contraseña: ")
    intentos=intentos-1

if intentos==0 and usuario_ingresado!=usuario and contraseña_ingresada!=contraseña:
    print("Inicio de sesion incorrecto, cuenta bloqueada")
else:
    print("Inicio de sesion correcto!")


#3. Escriba un programa que muestre el siguiente menú principal:
#1)	Calcular factorial
#2)	Calcular sumatoria
#3)	Salir

Salir="NO"

while Salir!="SI":
    print("¿Que desea realizar?")
    print("1) Calcular factorial")
    print("2) Calcular sumatoria")
    print("3) Salir")
    opcion=int(input("Ingrese su opcion (1, 2 o 3): "))
    if opcion==1:
        numero=int(input("Ingrese un numero: "))
        factorial=1
        for num in range(2, numero+1):
            factorial=factorial*num
        print(f"El factorial es: {factorial}")
    elif opcion==2:
        numero=int(input("Ingrese un numero: "))
        sumatoria=0
        for i in range(numero+1):
            sumatoria=sumatoria+i
        print(f"La sumatoria es: {sumatoria}")
    elif opcion==3:
        Salir="SI"
        #break (Tambien se puede utilizar el comando break para salir del ciclo)
    else:
        print("Opcion no encontrada.")

#Listas

Lista=[]
Lista=[3,4,5,6]
Lista=["hola","chao","diego"]
Lista=[3.4,4.4,5.2,6.5]
Lista=[3,4.4,"hola"]

#PRIMERA FORMA RECORRER LISTA
for i in Lista:
    print(i)

#SEGUNDA FORMA RECORRER LISTA
for i in range(len(Lista)):
    print(Lista[i])

#Creacion de una lista

Notas=[]
nota1=float(input("Ingrese la nota N°1: "))
nota2=float(input("Ingrese la nota N°2: "))
nota3=float(input("Ingrese la nota N°3: "))

Notas.append(nota1)
Notas.append(nota2)
Notas.append(nota3)

print(Notas)

#1. Crear una lista con n notas

nnotas=int(input("Cuantas notas desea ingresar a la lista: "))
Lista_notas=[]

for i in range(nnotas):
    nota=float(input(f"Ingrese la nota N°{i+1}: "))
    Lista_notas.append(nota)

print(Lista_notas)

#2. Llenar una lista con 5 numeros enteros y despues mostrar la raiz cuadrada, el numero al cuadrado y al cubo

Lista=[]

for i in range(5):
    numero=int(input(f"Ingrese el N°{i+1}: "))
    Lista.append(numero)

for i in range(len(Lista)):
    print(f"La raiz cuadrada del N°{i+1} es: {Lista[i]**(1/2)}")
    print(f"El cuadrado del N°{i+1} es: {Lista[i]**2}")
    print(f"El cubo del N°{i+1} es: {Lista[i]**3}")

#3. Llenar una lista con 5 numeros enteros, mostrarla y luego ordenarlos de mayor a menor

Lista=[]

for i in range(5):
    numero=int(input(f"Ingrese el N°{i+1}: "))
    Lista.append(numero)

print(Lista)
Lista.sort()
print(Lista)