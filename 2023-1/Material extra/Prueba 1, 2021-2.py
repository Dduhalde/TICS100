porcentaje=0
contador=0
promedio=0
while True:
    contador=+1
    nota1=(input(f"Ingrese la nota número {contador} (Escriba salir o Salir para terminar el programa): "))
    if nota1!="Salir" and nota1!="salir":
        nota2=float(nota1)
    if nota1=="Salir" or nota1=="salir":
        print(f"Su promedio final es: {promedio}")
        break
    elif nota2>7:
        ponderacion = int(input(f"Ingrese ponderación (entre 1-100) nota número {contador}: "))
        porcentaje=porcentaje+ponderacion
        if porcentaje>100:
            print("ERROR: !!Su ponderación suma más de 100!!")
        print("ERROR: !!Ingresó nota mayor a 7!!")
        promedio=promedio+nota2*(ponderacion/100)
        print(f"Su promedio final es: {promedio}")
        break
    else:
        ponderacion=int(input(f"Ingrese ponderación (entre 1-100) nota número {contador}: "))
        porcentaje = porcentaje + ponderacion
        if porcentaje>100:
            print("ERROR: !!Su ponderación suma más de 100!!")
            promedio = promedio + nota2 * (ponderacion / 100)
            print(f"Su promedio final es: {promedio}")
            break
        promedio=promedio+nota2*(ponderacion/100)

buenas=0
totales=0
while True:
    valor_1=int(input("Cuál es el primer valor a multiplicar? (-1 si desea salir): "))
    if valor_1==-1:
        porcentaje=(buenas/totales)*100
        print(f"Porcentaje de acierto: {porcentaje}%")
        break
    else:
        totales+=1
    valor_2=int(input("Cuál es el segundo valor a multiplicar?: "))
    resultado=int(input(f"Cuantos son {valor_1}x{valor_2}: "))
    if resultado==(valor_1*valor_2):
        buenas+=1


iteraciones=int(input("Ingrese la cantidad de iteraciones: "))
print(f"El programa calculará e con {iteraciones} iteraciones")
lista=[]
for i in range(1,iteraciones+1):
    lista.append(1/(i**2))
pi=(6*sum(lista))**(1/2)
print(f"PI calculado con {iteraciones} iteraciones es: {pi}")