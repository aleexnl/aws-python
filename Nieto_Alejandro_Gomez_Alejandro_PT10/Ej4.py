import random  # Importamos libreria


def baraja_mezclada():  # Iniciamos la funcion
    baraja = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'Sota', 'Caballo', 'Rey']  # Definimos una lista
    print("La baraja esta en orden: ")  # Mostramos mensaje
    print(baraja)  # Mostramos la lista
    print("Baraja mezclada: ")  # Mostramos mensaje
    random.shuffle(baraja)  # Mezclamos la baraja
    print(baraja)  # Mostramos la baraja (ahora mezclada)


baraja_mezclada()  # Llamamos a la funcion
