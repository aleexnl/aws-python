lst = []  # Iniciamos lista
psc = int(input("Introduce posicion: "))  # Pedimos valor
qty = int(input("Introduce cantidad de nombres a introducir: "))  # Pedimos cantidad
'''Este bucle lo que hara es pedir tantos nombres como se le ha indicado en el input anterior.'''
for i in range(qty):  # Iniciamos bucle
    lst.append(input("Introduce un nombre: "))  # Pedimos un valor y lo indexamos en una lista
'''Este bucle lo que hará es empezar a imprimir los nombres a partir de la posicion que se ha 
indicado basandose en el largo de la lista'''
for psc in range(len(lst)):
    print("Querido", lst[psc], "me alegro de verte")
