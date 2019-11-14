import random  # Importamos libreria


def juegodados():  # Definimos la funcion
    anna = 9  # Iniciamos variable
    bernat = 9  # Iniciamos variable
    while anna > 0 and bernat > 0:  # Mientras tengan puntos estamos en el bucle
        dado = random.randint(1, 6)  # Tiramos el dado
        print("¡Ha salido un ", dado, " !")  # Mostramos el resultado del dado
        if dado % 2 != 0:  # Si no es par pasara esto:
            anna = anna + dado  # Anna gana puntos basados en el dado
            bernat = bernat - dado  # Bernat pierde puntos basado en el dado
            print("Anna gana ", dado, " puntos")  # Muestra mensaje puntos ganados
            print("Bernat pierde ", dado, " puntos")  # Mestra mensaje puntos perdidos
            print("Puntos de Anna: ", anna)  # Muestra puntos actuales de Anna
            print("Puntos de Bernat: ", bernat)  # Muestra puntos actuales de Bernat
        else:  # Si el numero es par:
            anna = anna - dado  # Anna pierde puntos basados en dado
            bernat = bernat + dado  # Bernat gana puntos basados en el dado
            print("Bernat gana ", dado, " puntos")  # Muestra puntos ganados
            print("Anna pierde ", dado, " puntos")  # Muestra puntos perdidos
            print("Puntos de Anna: ", anna)  # Muestra puntos actuales de Anna
            print("Puntos de Bernat: ", bernat)  # Muestra puntos actuales de Bernat
    print("Puntos de Anna: ", anna)  # Mostramos puntos finales de Anna
    print("Puntos de Bernat: ", bernat)  # Mostramos puntos finales de Bernat


print("JUEGO DE LOS DADOS\n")  # Mostramos titulo
start = int(input("¿Quieres jugar al juego de los dados?:(1:SI/2:NO) "))  # Preguntamos si quieren jugar
while start == 1:  # Mientras quieran jugar:
    juegodados()  # Iniciamos juego
    start = int(input("¿Quieres volver a jugar al juego de los dados?:(1:SI/2:NO) "))  # Preguntamos si quieren jugar
print("¡Hasta la próxima!")  # Nos despedimos.
