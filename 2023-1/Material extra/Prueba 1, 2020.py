#Pregunta 1


a=int(input("Ingrese numero 1: "))
b=int(input("Ingrese numero 2: "))
i=1
resto = 0
if b>a:
    while(b > 0):
        resto = b
        b = a % b
        a = resto
    if a==1:
        print("son coprimos")
    else:
        print("no son coprimos")
else:
    while(a > 0):
        resto = a
        a = b % a
        b = resto
    if b==1:
        print("son coprimos")
    else:
        print("no son coprimos")

#
#
#
#Pregunta número 2
#
#
#

qty_numbers = int(input("Ingresa la cantidad de números de Fibonacci a generar:  ")) # Obtener cantidad de números Fibonacci a generar 

fibonacci_list = [] # Se crea lista para guardar la serie de Fibonacci

for i in range(qty_numbers): # Se itera en la cantidad de números solicitada
    if i == 0: # Se verifica si es la primera iteración para incorporar el número 0 a la lista de Fibonacci
        current = 0
    elif i in [1, 2]: # Se verifica si es la segunda y tercera iteración para incorporar el número 1 a la lista de Fibonacci
        current = 1
    else:
        current = fibonacci_list[-1] + fibonacci_list[-2] # Se suman los últimos 2 números de la serie de Fibonacci para incorporarlo a la lista
    fibonacci_list.append(current) # Se incorpora el número de Fibonacci correspondiente a la iteración

print(fibonacci_list) # Se imprime la lista de Fibonacci obtenida

count = 0 # Se crea un contador para obtener los números que pertenecen a la serie de Fibonacci generada

number = 1 # Se fija un número positivo para activar la iteración 
while number >= 0: # Si el número es menor que cero la iteración se cierra
  number = int(input("Ingresa un número a evaluar:  ")) # Se solicita el número a evaluar al usuario

  if number in fibonacci_list: # Se verifica si el número está en la lista de Fibonacci generada
    count += 1 # Si el número está en la lista se suma uno al contador
  
print(f"La cantidad de números ingresados que son de la serie de Fibonacci son : {count}") # Se imprime la cantidad de números ingresados por el usuario que se encuentran en la lista de Fibonacci generada
  
#
#
#
#Pregunta número 3
#
#
#

sentence = input("Ingrese la frase a cambiar: ") # Se solicita la frase al usuario

change_letter = input("Ingrese la vocal que se escribirá: ") # Se solicita la vocal que reemplazara el resto de las vocales

vocals = ["a", "e", "i", "o", "u"] # Se genera un arreglo con las vocales

new_sentence = "" # Se crea variable para guardar la frase nueva

for letter in sentence: # Se recorren las letras de la frase

  if letter in vocals: # Se verifica si la letra es una vocal
    new_sentence += change_letter # Si la letra es una vocal se reemplaza por change_letter y se suma a la nueva frase
  else:
    new_sentence += letter # Si la letra no es una vocal se suma la letra a la nueva frase

print(f"Resultado: {new_sentence}") # Se imprime la nueva frase con las vocales reemplazas

