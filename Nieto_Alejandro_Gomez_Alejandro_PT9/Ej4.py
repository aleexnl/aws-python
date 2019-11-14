# Importamos la funcion random
import random
# Creamos las variables donde se van a contar las veces ganadas y perdidas
ganadas=0
perdidas=0
# Entramos en el bucle
while True:
    #Definimos las variables A y B donde tendran un numero aleatorio dentro.
    a=random.randrange(1, 11)
    b=random.randrange(1, 11)
    #Pediremos al jugador por quien apuesta
    jugador=input("Por quien apuestas por A o por B: ")
    # Definimos las condiciones para saber si a puesto bien la opción
    if jugador=="A" or jugador=="B":
        #Definimos las condiciones para saber si a ganado a a perdido o los numeros son los mismos
        if (jugador=="A" and a>b) or (jugador=="B" and b>a):
            # Sumamos 1 al contador ganadas y le decimos al usuario que ha ganado y cuantas tiene ganadas y perdidas
            ganadas=ganadas+1
            print("A vale "+str(a)+" y B vale "+ str(b))
            print("¡Has ganado!")
            print("Llevas "+str(ganadas)+" ganadas, y "+str(perdidas)+" perdidas")
            # Le preguntamos si quiere volver a jugar, y que si es asi que le de a 1 y sino a cualquier tecla.
            jugar =input("Si quieres volver a jugar presione 1 sino presiona otra tecla: ")
            if jugar != 1:
                break
        elif a==b:
            print("Son los mismos numeros. ¡Vuelvan a apostar!")
        else:
            # SUmamos 1 al contador de perdidas y le decimos al usuario que ha perdido y le decimos cuantas ha ganado y cuantas a perdido
            perdidas=perdidas+1
            print("A vale "+str(a)+" y B vale "+ str(b))
            print("¡Has perdido!")
            print("Llevas "+str(ganadas)+" ganadas, y "+str(perdidas)+" perdidas")
            # Y al igual que si gana le pedimos si quiere volver a jugar
            jugar = input("Si quieres volver a jugar presione 1 sino presiona otra tecla: ")
            if jugar != 1:
                break
    # Si no ha puesto bien la opcion se lo informamos y como es un bucle empezara de nuevo.
    else:
        print("Opcion no valida, compruebe que la letra esta en mayuscula y sea A o B")
# Cuando no quiera jugar mas se acabara el programa y le diremos adios.
print("Bye")


