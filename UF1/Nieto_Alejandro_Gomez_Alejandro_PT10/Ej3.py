import random  # Importamos la libreria


def generadorcustom():  # Definimos la función.
    # Pedimos el numero limite para el generador.
    x = int(input("Introduce un numero entero como limite para el generador: "))
    while x <= 0:  # Comprobamos que sea mayor que 0
        print("¡Introduce un numero entero mayor que 0!")  # Mostramos error.
        # Pedimos el numero limite para el generador hasta que sea aceptado.
        x = int(input("Introduce un numero entero como limite para el generador: "))
    num = random.randrange(0, x+1, 2)  # Generamos una variable random del 0 al x con impas de 2.
    print("El numero aleatorio es: ", num)  # Mostramos el numero generado.


generadorcustom()  # Llamamos a la función.
