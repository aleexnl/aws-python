import os  # Importamos libreria
bibliografia = {}  # Iniciamos el diccionario
var = int(input("Introduce un codigo ID de 4 numeros: "))  # Pedimos valor
while var < 0:  # Comprobamos que sea un valor valido
    print("Longitud no valida!")  # Imprimimos error
    var = int(input("Introduce un codigo ID de 4 numeros: "))  # Pedimos valor
bibliografia["IDLibro"] = var  # Adjuntamos el valor al diccionario

'''Da mucho palo comentar todo esto porque es lo mismo todo el rato. Espero que lo entendais profes
Alejandro Nieto <3'''

var = str(input("Introduce el titulo del libro: "))
bibliografia["Titulo de libro"] = var
var = str(input("Introduce el autor: "))
bibliografia["Titulo de autor"] = var
var = str(input("Introduce la editorial: "))
bibliografia["Titulo de editorial"] = var
var = int(input("Introduce el año de edicion: "))
while var < 0:
    print("Longitud no valida!")
    var = int(input("Introduce el año de edicion: "))
bibliografia["Año de edicion"] = var
var = int(input("Introduce las paginas del libro: "))
while var < 0:
    print("Longitud no valida!")
    var = int(input("Introduce las paginas del libro: "))
bibliografia["Paginas del libro"] = var
os.system('cls')  # Limpiar terminal en Windows
os.system('clear')  # Limpiar terminal en Linux
print(bibliografia)  # Mostramos el diccionario
