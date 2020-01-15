from modules import functions as fc # Importamos la funcion que hemos creado.

while True: # Creamos un bulce infinito del cual no podamos salir hasta que el numero sea entero.
    try:
        num = int(input("Introduce un numero: "))
        break
    except ValueError: # Si el numero es decimal nos enseñara este mensaje de error.
        print("ERROR: Introduce solo valores enteros")

while True:
    try:
        num2 = int(input("Introduce un numero: "))
        break
    except ValueError:
        print("ERROR: Introduce solo valores enteros")

print(fc.rus(num,num2)) # Llamamos a la funcion y sustituimos los valores por estos.
