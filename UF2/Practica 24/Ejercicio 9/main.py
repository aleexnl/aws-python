from module import functions as fc

while True: # Creamos un bulce infinito del cual no podamos salir hasta que el numero sea entero.
    try:
        num = int(input("Introduce un numero: "))
        break
    except ValueError: # Si el numero es decimal nos enseñara este mensaje de error.
        print("ERROR: Introduce solo valores enteros")

while True: # Creamos un bulce infinito del cual no podamos salir hasta que el numero sea entero.
    try:
        num2 = int(input("Introduce un numero: "))
        break
    except ValueError: # Si el numero es decimal nos enseñara este mensaje de error.
        print("ERROR: Introduce solo valores enteros")

print(fc.combinatorio(num,num2))