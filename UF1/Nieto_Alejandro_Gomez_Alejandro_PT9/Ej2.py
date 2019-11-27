# Importamos la función random
import random
# Iniciamos la variable de el numero al azar del 1 al 100
num = random.randint(1, 100)
# Iniciamos el contador a 5
contador = 5

print("ADIVINA EL NUMERO DEL 1 AL 100")
# Pedimos el numero al usuario
numuser = int(input("Introduce un numero del 1 al 100: "))
# Comparamos;
# Mientras el input es distinto y el contador no sea 0
# Mostramos cuantos intentos quedan y que vuelva a intentar
while numuser != num and contador != 1:
    contador = contador - 1
    print("Te quedan ", contador, " Intentos")
    numuser = int(input("Introduce un numero del 1 al 100: "))
# Comparador al salir del bucle
# Si se ha quedado sin intentos
if contador == 0:
    print("No has acertado")
# si ha acertado
elif numuser == num:
    print("Has acertado, el numero era: ", num)
# Cualquier otra cosa
else:
    print("No has acertado :(")
