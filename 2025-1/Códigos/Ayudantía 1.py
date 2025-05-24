# Ayudantía 1
# Diego Duhalde dduhalde@alumnos.uai.cl

# prints
print("Nombre:", "Juan")
print("Edad:", 19)
print("Altura:", 1.71)
print("¿Es universitario?", True)

# Concatenación de strings
print("Hola, soy " + "Juan" + " y tengo " + "19" + " años")
print("Python, " + "es " + "un " + "lenguaje " + "de " + "programación")

# Más funcionalidades
print("Uno\nDos\nTres") # \n es un salto de línea
print("Uno\n\tDos\n\t\tTres") # \t es un tabulador
print("Hola mundo\rPython") # \r es un retorno de carro (Cambia lo que se encuentre a la derecha por lo que se encuentra a la izquierda)
print("123456789\r987")
print("Holaaa\b!") # \b es un retroceso (Borra el caracter anterior, borra una a)

# Parametro extra
print("Rojo", "Verde", "Azul", sep=" - ") # sep es un parámetro extra que se le puede pasar a la función print, por defecto es sep=" "
print("Rojo", "Verde", "Azul", sep=" - ", end=" - ") # end es un parámetro extra que se le puede pasar a la función print, por defecto es end="\n"  (salto de línea)
print("Prueba de que este print no salto de linea")