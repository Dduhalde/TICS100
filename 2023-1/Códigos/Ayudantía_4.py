#dduhalde@alumnos.uai.cl

#Preparación prueba 1

#Pregunta 1, Prueba 1 Simulacro 2021/1
edad=int(input("Ingrese su edad: "))
estudiante=input("Es estudiante? (Si/No): ")
salud=input("Trabajador de la salud? (Si/No): ")
caja=input("Eres socio de la caja de los andes? (Si/No): ")

if salud=="Si" and caja=="Si":
    print(f"El precio de su entrada es: {(5000*0.3)*0.7}")
elif edad>60 and caja=="Si":
    print(f"El precio de su entrada es: {(5000*0.4)*0.7}")
elif estudiante=="Si" and caja=="Si":
    print(f"El precio de su entrada es: {(5000*0.5)*0.7}")
elif salud=="Si":
    print(f"El precio de su entrada es: {(5000*0.3)}")
elif edad>60:
    print(f"El precio de su entrada es: {(5000*0.4)}")
elif estudiante=="Si":
    print(f"El precio de su entrada es: {(5000*0.5)}")
elif caja=="Si":
    print(f"El precio de su entrada es: {(5000*0.7)}")
else:
    print(f"El precio de su entrada es: {(5000)}")

#Pregunta 2, Prueba 1 2019/2

precio=int(input("Ingrese el precio del automóvil: "))
tipo=int(input("Ingrese el tipo de automóvil (0 para gasolina o diesel, 1 para híbrido, 2 para eléctrico): "))
if tipo==0:
    precio=precio*1.25
elif tipo==1:
    precio=precio*1.15
elif tipo==2:
    precio=precio*1.05
if precio>20000000:
    print("Tiene impuesto al lujo")
    precio=precio*1.10
print(f"El precio final es de: {round(precio, 2)}")

#Pregunta 3, Prueba 1 Simulacro 2021/1 "Ejercicio dificil, mucha logica"
Rut=input("Ingresa tu Rut para calcular el digito verificador: ")
Factor=2
Suma=0
for i in range(len(Rut)-1,-1,-1):
    Suma=Suma+int(Rut[i])*Factor
    Factor=Factor+1
    if Factor==8:
        Factor=2
DivisionEntera=int(Suma/11)
Multiplicar=DivisionEntera*11
Resta=Suma-Multiplicar
DigitoVerificador=11-Resta
if DigitoVerificador==10:
    DigitoVerificador="K"
print(f"El Rut es: {Rut}-{DigitoVerificador}")


#Pregunta 1, Prueba 1 Simulacro 2022/1

calle=input("Ingrese el nombre de la calle/avenida: ")
velocidad=int(input("Ingrese la velocidad: "))

if calle=="Siempre Viva":
    if velocidad<50:
        gravedad="Sin Infracción"
        multa="$0"
        minmulta=0
        maxmulta=0
    elif velocidad>70:
        gravedad="Falta gravísima"
        multa="Entre $250 y $700 inclusive"
        minmulta=250
        maxmulta=700
    else:
        gravedad="Falta grave"
        multa="Entre $100 y $200 inclusive"
        minmulta=100
        maxmulta=200
elif calle=="Ruta 6":
    if velocidad<140:
        gravedad="Sin Infracción"
        multa="$0"
        minmulta=0
        maxmulta=0
    else:
        gravedad="Falta gravísima"
        multa="Entre $500 y $1.000 inclusive"
        minmulta=500
        maxmulta=1000
elif calle=="Padre Diagonal":
    if velocidad<50:
        gravedad="Sin Infracción"
        multa="$0"
        minmulta=0
        maxmulta=0
    else:
        gravedad="Falta grave"
        multa="Entre $300 y $400 inclusive"
        minmulta=300
        maxmulta=400

print(f"{gravedad} en {calle} al conducir a una velocidad de {velocidad} km/h")

if gravedad!="Sin Infracción":
    valormulta=int(input(f"Ingrese el valor de la multa, esta debe ser un valor {multa}: "))
    if valormulta>=minmulta and valormulta<=maxmulta:
        pass
    else:
        print("El valor ingresado es erróneo.")

#Pregunta 2, Prueba 1 Simulacro 2022/1

tipopizza=input("Ingrese el tipo de Pizza (XXL, XL, L o S): ")
cantpizza=int(input(f"Ingrese el número de pizzas {tipopizza}: "))

if tipopizza=="XXL":
    for i in range(cantpizza):
        nombre1=input("Ingrese nombre 1: ")
        nombre2=input("Ingrese nombre 2: ")
        nombre3=input("Ingrese nombre 3: ")
        nombre4=input("Ingrese nombre 4: ")
        print(f"Pizza {i+1}: {nombre1}, {nombre2}, {nombre3}, {nombre4}")
elif tipopizza=="XL":
    for i in range(cantpizza):
        nombre1=input("Ingrese nombre 1: ")
        nombre2=input("Ingrese nombre 2: ")
        nombre3=input("Ingrese nombre 3: ")
        print(f"Pizza {i+1}: {nombre1}, {nombre2}, {nombre3}")
elif tipopizza=="L":
    for i in range(cantpizza):
        nombre1=input("Ingrese nombre 1: ")
        nombre2=input("Ingrese nombre 2: ")
        print(f"Pizza {i+1}: {nombre1}, {nombre2}")
elif tipopizza=="S":
    for i in range(cantpizza):
        nombre1=input("Ingrese nombre 1: ")
        print(f"Pizza {i+1}: {nombre1}")

#Pregunta 3, Prueba 1 Simulacro 2022/1

numcolores=int(input("Ingrese el número de colores distintos: "))
numquitasoles=int(input("Ingrese el número de quitasoles: "))

if numquitasoles<10:
    print("Esto no prendió", end="")
elif numquitasoles>=10 and numquitasoles<=20:
    print("Está prendiendo la cosa", end="")
elif numquitasoles>20 and numquitasoles<50:
    print("Esto se está saliendo de control", end="")
else:
    print("Ya perdimos el control", end="")
for i in range(numcolores*3):
    print("!", end="")

N=numcolores*numquitasoles*4.5+300
print("")
if N<500:
    print(f"El factor N es {N}, la municipalidad estudiará poner publicidad en las ciudades cercanas para que acudan más personas.")
elif N>500:
    print(f"El factor N es {N}, se espera que la municipalidad limite el ingreso de más bañistas a la playa para regular el aforo de esta")