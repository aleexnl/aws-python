psc = int(input("Introduce posicion: "))  # Pedimos valor
qty = int(input("Introduce cantidad de nombres a introducir: "))  # Pedimos cantidad
lst = [] # Iniciamos lista
'''Este bucle lo que hara es pedir tantos nombres como se le ha indicado en el input anterior.'''
for i in range(qty):  # Iniciamos bucle
    while True:
        l=[]
        nom=(input("Introduce un nombre: "))  # Pedimos un valor y lo indexamos en una lista
        gen = int(input("Escribe 1 si eres hombre y 2 si eres mujer "))  # Pedimos el genero
        if gen == 1: # Si gen es igual a 1 añadiremos a la 2 lista vacia la cadena Hombre
            l.append(nom)
            l.append("Hombre")
            lst.append(l)
            break
        elif gen == 2: # Si es 2 añadiremos Mujer
            l.append(nom)
            l.append("Mujer")
            lst.append(l)
            break
        else: # Si no es un campo valido y lo vuelve a pedir
            print("Campo no valido")
        print(l)

'''Este bucle lo que hará es empezar a imprimir los nombres a partir de la posicion que se ha 
indicado basandose en el largo de la lista'''
for psc in range(len(lst)):
    if lst[psc][1] == "Hombre":
        print("Querido", lst[psc][0], "me alegro de verte")
    else:
        print("Querida", lst[psc][0], "me alegro de verte")

