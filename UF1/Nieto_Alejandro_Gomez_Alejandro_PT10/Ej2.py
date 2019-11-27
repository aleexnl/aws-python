import random  # Importamos la libreria.


def generadorpares():  # Definimos la función
    for i in range(100):  # mostraremos una secuencia de 100 numeros pares al azar
        print(random.randrange(0, 101, 2))  # Mostramos el numero generado.


generadorpares()  # Llamamos a la función.
