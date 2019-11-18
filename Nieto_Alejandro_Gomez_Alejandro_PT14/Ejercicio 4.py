# Copyright 2019 Alejandro Nieto Luque - AWS 1
# Copyright 2019 Aaron Martos - AWS 1
import random  # Importamos libreria
llistanumerosAleatoirs = []  # Iniciamos variable de lista
llistaDistancies = []  # Iniciamos variable de lista
'''Este bucle va a generar 20 numeros aleeatorios del 0 al 9 y los va a añadir en una lista'''
for i in range(20):  # Iniciamos bucle contado
    llistanumerosAleatoirs.append(random.randint(0, 9))  # Añadimos numero aleatorio a lista
x = random.randint(5, 10)  # Variable con numero aleatorio
for i in range(x):
    llistaDistancies.append(0)
    for j in llistanumerosAleatoirs:
        llistaDistancies[i] += i-j
for i in range(x):
    print(i, "--> ", llistaDistancies[i], " ", end="")
    for j in range(llistaDistancies[i]):
        print("*", end="")
    print()
