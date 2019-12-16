llista_paraules = []  # Fem una llista per guardar les paraules


def paraules(llista):  # definim la funcio per saber les paraules repetides
    duplicated = []  # Definimos lista para los valores duplicados
    for valor in llista:  # per cada paraula en la llista
        if llista.count(valor) > 1:  # si la paraula es trobada mes de un cop a la llista
            if valor not in duplicated:  # Comprueba si no esta en la lista de duplicados
                duplicated.append(valor)  # Añade el valor a la lista
    return duplicated  # Devuelve la lista


while True:  # Bucle infinito que solo se rompe si se pone fi
    paraula = input('Introdueix una paraula:')
    if str.upper(paraula) != 'FI':  # Condicion para si la palabra no es fin
        llista_paraules.append(paraula)  # Añadir palabra a la lista
    elif str.upper(paraula) == 'FI':  # Condicion de la palabra fi acaba el bucle
        break  # Acabar el bucle
print("Palabras duplicadas: ", paraules(llista_paraules))  # Mostramos la funcion
