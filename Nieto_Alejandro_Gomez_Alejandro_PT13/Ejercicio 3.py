psc = int(input("Introduce posicion: "))  # Pedimos valor
qty = int(input("Introduce cantidad de nombres a introducir: "))  # Pedimos cantidad
lst = [[]] # Iniciamos lista
'''Este bucle lo que hara es pedir tantos nombres como se le ha indicado en el input anterior.'''
for i in range(qty):  # Iniciamos bucle
    while True:
        lst[i].append(input("Introduce un nombre: "))  # Pedimos un valor y lo indexamos en una lista
        gen = int(input("Escribe 1 si eres hombre y 2 si eres mujer "))  # Pedimos un valor y lo indexamos en una lista
        if gen == 1:
            lst[i].append("Hombre")
            break
        elif gen == 2:
            lst[i].append("Mujer")
            break
        else:
            print("Campo no valido")
    print(i)
    print(lst)
'''Este bucle lo que hará es empezar a imprimir los nombres a partir de la posicion que se ha 
indicado basandose en el largo de la lista'''
for psc in range(len(lst)):
    if lst[psc][1]:
        print("Querido", lst[psc], "me alegro de verte")
    else:
        print("Querida", lst[psc], "me alegro de verte")
print(lst)

'''
lst=[0, [1,2], 2]
lst[1].append(5)
print(lst)
'''
