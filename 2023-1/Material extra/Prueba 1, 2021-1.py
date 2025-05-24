#Código que resuelve las preguntas de la prueba.

#Pregunta 1
pizzaA=0
pizzaV=0
pizzaI=0
pizzaG=0
print("Bienvenido al sistema de evaluación de pizzas")
respuesta=input("Ingrese notas en formato 4331 o 0 para terminar:")
contador=0
while respuesta!='0':
  pizzaV+=int(respuesta[0])
  pizzaA+=int(respuesta[1])
  pizzaI+=int(respuesta[2])
  pizzaG+=int(respuesta[3])
  respuesta=input("Ingrese notas en formato 4331 o 0 para terminar:")
  contador=contador+1
print(f"Nota de la pizza Villarrica: {pizzaV/contador}")
print(f"Nota de la pizza Antuco: {pizzaA/contador}")
print(f"Nota de la pizza Icalma: {pizzaI/contador}")
print(f"Nota de la pizza Galletué: {pizzaG/contador}")

#Pregunta 2
nombre=input("Ingrese el nombre del cliente: ")
direccion=input("¿Se comprobó la dirección del cliente? Si/No ")
identidad=input("¿Se comprobó la identidad del cliente? Si/No ")
saldo=input("¿El monto del préstamo es menor al saldo mensual? Si/No ")
proposito=input("Ingrese el propósito del préstamo: (1) Comprar casa (2) Pago impuestos (3) otros ")
casa=input("¿El cliente es propietario de una casa? Si/No ")
if direccion!='No' and identidad!='No':
    if saldo=='Si':
      print(f"La solicitud de {nombre} ha sido aprobada")
    else:
      if proposito=='2':
        print(f"La solicitud de {nombre} ha sido aprobada")
      elif proposito=='3':
        print("Se deben pedir más antecedentes")
      else:
        if casa=='Si':
          print(f"La solicitud de {nombre} ha sido aprobada")
else:
  print(f"La solicitud de {nombre} ha sido rechazada")

#Pregunta 3
sexo=input("Ingrese su sexo H/M o escriba Salir para finalizar: ")
if sexo!='Salir':
  peso=float(input("Ingrese su peso en Kg: "))
  altura=float(input("Ingrese su altura en cm: "))
  edad=float(input("Ingrese su edad en años: "))
  print("según la siguiente tabla usted hace:")
  print("   a) Poco o nada de ejercicio")
  print("   b) Ejercicio ligero, 1 a 3 días a la semana")
  print("   c) Ejercicio moderado, 3 a 5 días a la semana")
  print("   d) Soy deportista, 6 a 7 días a la semana")
  print("   e) Soy atleta, entrenamiento mañana y tarde")
  respuesta=input("Alternativa a, b, c, d, e?: ")
  if sexo=='M':
    TMB= 655 + 9.6*peso + 1.8*altura-4.7*edad
  else:
    TMB = 66 + 13.7*peso + 5*altura - 6.75*edad

  if respuesta=='a':
    TMB*=1.2
  elif respuesta=='b':
    TMB*=1.375
  elif respuesta=='c':
    TMB*=1.55
  elif respuesta=='d':
    TMB*=1.72
  elif respuesta=='e':
    TMB*=1.9

  print(f"Su TMB es de {TMB}")
  print("¿Desea conocer cómo esta su alimentación? a) Si b) Salir del programa")
  respuesta=input("¿Qué opción desea? a/b: ")
  while respuesta=='a':
    hidratosCarbono=float(input("¿cuántos gramos de hidrato de carbono consume al día?: "))
    proteina=float(input("¿cuántos gramos de proteínas consume al día?: "))
    grasa=float(input("¿cuántos gramos de grasa consume al día?: "))
    consumoCalorias=4*(hidratosCarbono+proteina)+9*grasa
    diferenciaCalorias=30*(TMB-consumoCalorias)
    if diferenciaCalorias>0:
      print("Ud consume menos calorías de las que gasta")
      print(f"Ud bajará {round(diferenciaCalorias/7000,2)} kg cada 30 días")
    else:
      print("Ud consume más calorías de las que gasta")
      print(f"Ud subirá {round(-diferenciaCalorias/7000,2)} kg cada 30 días")
    print("¿Desea conocer cómo esta su alimentación? a) Si b) Salir del programa")
    respuesta=input("¿Qué opción desea? a/b: ")
  print('Hasta luego')    
else:
  print('Hasta luego')
