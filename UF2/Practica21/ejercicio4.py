def comparador(l1, l2):
    duplicated = []
    for k in range(len(l1)):
        if l1[k] in l2:
            if l1[k] not in duplicated:
                duplicated.append(l1[k])
    for j in range(len(l2)):
        if l2[j] in l1:
            if l2[j] not in duplicated:
                duplicated.append(l2[j])
    print(duplicated)


lista_1 = []
lista_2 = []

while True:
    try:
        qty = int(input("Introduce la cantidad de elementos a introducir en la lista 1:"))
        if qty > 0:
            break
        if qty <= 0:
            print("¡Introduce un valor mayor que 0!")
    except ValueError:
        print("¡Introduce solo valores enteros!")
for i in range(qty):
    tmp = input("Introduce el valor a añadir en lista 1: ")
    lista_1.append(tmp)

while True:
    try:
        qty = int(input("Introduce la cantidad de elementos a introducir en la lista 2:"))
        if qty > 0:
            break
        if qty <= 0:
            print("¡Introduce un valor mayor que 0!")
    except ValueError:
        print("¡Introduce solo valores enteros!")
for i in range(qty):
    tmp = input("Introduce el valor a añadir en lista 2: ")
    lista_2.append(tmp)
comparador(lista_1, lista_2)
