import random
''' Creamos las dos listas vacias '''
llistaAleatoris = []
llistaComptadorNumerosAleatoris = []
''' Y creamos dos fors anidados '''
for i in range(random.randint(5, 10)): # En este hacemos que escoja aleatoriamente cuantas veces va a hacer el proceso entre 5 y 10
    for j in range(20): # Y aqui hacemos que se añada a la lista de aleatorios un numero entre 0 y 9, y que lo haga 20 veces
        llistaAleatoris.append(random.randint(0, 9))

for i in range(10): # Y aqui hacemos que cuente todos los numeros del 0 al 9 y lo vaya poniendo en una lista y ordenadamente.
    llistaComptadorNumerosAleatoris.append(llistaAleatoris.count(i))

''' Y aqui finalmente printaremos la pantalla con la cantidad que sale cada numeros y esa misma cantidad en asteriscos al lado '''
for i in range(10):
    print(i, "--> ", llistaComptadorNumerosAleatoris[i], " ", end="")

    for j in range(llistaComptadorNumerosAleatoris[i]):
        print("*", end="")


    print() # Este print de aqui lo que hara es que ponga una cosa encima de otra