# En esta parte iniciamos las listas de variables
lst1 = []
lst2 = []
lst1words = []
lst2words = []
duplicated = []
count = 0
# Cantidad de numeros a ingresar en lista1
qty = int(input("Introduce cantidad de palabras a introducir en la Lista1: "))
while qty < 1:  # Comprueba que el numero sea mayor que 0
    print("Error, introduce un valor mayor que 0")  # Muestra error
    qty = int(input("Introduce cantidad de palabras a introducir en la Lista1: "))  # Pedir valor
for i in range(qty):  # Bucle para añadir tantas palabras como se han indicado antes
    wrd = str(input("Introduce una palabra para añadir: "))  # Pedimos palabra
    lst1.append(wrd)  # Agregamos el valor a la lista
print("\n")  # ESPACIADOR
qty = int(input("Introduce cantidad de palabras a introducir en la Lista2: "))  # Pedir valor
while qty < 1:  # Comprueba que el numero sea mayor que 0
    print("Error, introduce un valor mayor que 0")  # Muestra error
    qty = int(input("Introduce cantidad de palabras a introducir en la Lista2: "))  # Pedir valor
for j in range(qty):  # Bucle para añadir tantas palabras como se han indicado antes
    wrd = str(input("Introduce una palabra para añadir: "))  # Pedimos palabra
    lst2.append(wrd)  # Agregamos el valor a la lista
i = 0
while i != len(lst1):
    while lst1.count(lst1[i]) != 1:
        lst1.remove(lst1[i])
    i += 1
i = 0
while i != len(lst2):
    while lst2.count(lst2[i]) != 1:
        lst2.remove(lst2[i])
    i += 1
for i in lst1:
    if i in lst2 and duplicated.count(i) < 1:
        duplicated.append(i)
    elif lst1words.count(i) < 1:
        lst1words.append(i)
for i in lst2:
    if i in lst1 and duplicated.count(i) < 1:
        duplicated.append(i)
    elif not(i in lst1) and lst2words.count(i) < 1:
        lst2words.append(i)
print("\n")  # Espaciador
print("En las dos listas: ", duplicated)  # Mostramos lista duplicados
print("Solo en la primera lista: ", lst1words)  # Valores unicos lista 1
print("Solo en la segunda lista: ", lst2words)  # Valores unicos lista 2

