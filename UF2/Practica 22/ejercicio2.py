# definim la funcio posicio lletra.
def pos_letra():
    paraula = input('Introdueix una paraula:')  # Pedimos al usuario una palabra.
    lletra = input('Introdueix una lletra per saber la seba posicio:')  # Pedimos una letra.

    if lletra not in paraula:  # Si la lletra introduida no es en la paraula.
        print('Error la lletra no es en la paraula.')  # Imprimira aquest missatge.

    for i in range(len(paraula)):  # Si pasa per cada posicdio de la paraula.
        if lletra == paraula[i]:  # si la lletra es a la paraula.
            posicio = paraula.index(lletra)  # guardem la posicio de la lletra en la variable posicio.
            print(posicio + 1)  # imprimim la variable i li sumem 1, ja que comença des de 0.


# cridem a la funcio pos_letra.
pos_letra()
