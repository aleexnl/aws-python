import random  # Importamos la libreria random
randabc = []  # Creamos la lista de las letras aleatorias
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
       "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]  # Definimos una lista con el abecedeario
randnum = []  # Creamos la lista de las letras aleatorias
'''Este bucle lo que hara sera crear 10 numeros aleatorios del 0 al 25, refiriendose al total de posiciones de 
la lista del abecedario'''
for i in range(10):  # Iniciamos bucle que se repetira 10 veces
    randnum.append(random.randint(0, 25))  # Genera numeros aleatorios y los añade a la lista
'''Este bucle lo que hará es pasar por todos los numeros de la lista de numeros aleatorios y añadir, 
segun el valor de la posicion de la lista'''
for i in range(len(randnum)):  # Iniciamos el bucle
    randabc.append(abc[randnum[i]])  # Añadimos el valor segun el valor de la posicion de la lista
print(randnum)  # Mostramos la lista de numeros aleatorios
print(randabc)  # Mostramos la lista de letras aleatorias
