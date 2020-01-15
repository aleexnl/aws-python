from modules import functions as fc # Importamos la funcion de functions.py

while True: # creamos un bucle infinito, del cual podremos salir cuando el numero sea entero.
    try:
        dividend = int(input("Introduce un dividendo: "))
        break
    except ValueError: # Si introducimos un numero decimal nos mostrara el mensaje.
        print("ERROR: Introduce solo valores enteros")

while True: # creamos un bucle infinito, del cual podremos salir cuando el numero sea entero.
    try:
        divisor = int(input("Introduce un divisor: "))
        break
    except ValueError: # Si introducimos un numero decimal nos mostrara el mensaje.
        print("ERROR: Introduce solo valores enteros")

print(fc.recursive_div(dividend, divisor))# Llamamos a la funcion y sustituimos sus valores por estos.
