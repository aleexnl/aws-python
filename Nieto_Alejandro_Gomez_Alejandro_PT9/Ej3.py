# Importamos la funcion random
import random
# Mostramos el menu con las diferentes armas y sus numeros asignados
print("Piedra -> 1")
print("Paper -> 2")
print("Tisoras -> 3")
# Entramos en el bucle directamente
while True:
    # Ahora los dos jugadores elegiran su arma, la maquina con la funcion random.randrage y al jugador se lo pediremos
    maquina=random.randrange(1, 4)
    jugador=int(input("Escull la teva arma: "))
    # Y definiremos los diferentes condicionales para saber si gana la maquina o el jugador
    if (jugador==1 and maquina==2) or (jugador==2 and maquina==3) or (jugador==3 and maquina==1):
        print("Has perdut")
        break
    elif (jugador==maquina):
        print("Empate, vuelve a probar")
    else:
        print("Has ganado")
        break
