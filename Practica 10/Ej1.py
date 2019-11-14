# Importamos la libreria
import random

# Definimos la funcion


def dados():
    # Mostramos mensaje
    print("Tirando dados...")
    # Iniciamos variables del 1 al 6
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    # Mostramos las variables
    print("Dado 1: ", d1)
    print("Dado 2: ", d2)


# Iniciamos la funcion
dados()
