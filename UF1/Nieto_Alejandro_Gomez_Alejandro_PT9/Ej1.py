# Importamos la función random
import random
# Iniciamos la variable de el numero al azar del 1 al 10
num = random.randint(1, 10)

print("ADIVINA EL NUMERO DEL 1 AL 10")
# Pedimos el numero al usuario
numuser = int(input("Introduce un numero del 1 al 10: "))
# Comparamos;
# Mientras el input es distinto, que muestre error y vuelva a intentar
while numuser != num:
    print("¡Este no es el numero!")
    numuser = int(input("Introduce un numero del 1 al 10: "))
# Mostramos acierto + el numero que era.
print("Has acertado, el numero era: ", num)
