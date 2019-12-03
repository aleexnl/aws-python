# Definir una funció superposicio() que tomi dos llistes i retorni true si tenen al menys 1 membre en comú o retorni
# false de lo contrari.


def superposicio(l1, l2):  # Iniciamos la funcion
    cont = 0  # Iniciamos un contador
    for i in range(len(l1)):  # Este bucle ira por todas las posiciones de la lista
        if l1[i] in l2:  # Si esa palabra de la posicion esta en la otra lista, le sumamos 1 al contador
            cont += 1  # Sumamos 1 al contador
    """ Una vez acabado el bucle lo que haremos serán dos condicionales que comprobaran el valor de la valirable
    contador. Si el contador es diferente a 0 este automaticamente mostrara un True, pero si no ha cambiado su valor
    simplemente se Mostrara un False """
    if cont != 0:  # Expresamos condicion
        return "True"  # Acabamos funcion
    elif cont == 0:  # Expresamos condicion alternativa
        return "False"  # Acabamos funcion


lista1 = ['Hola', 'Adios', 'Buenos dias', 'Buenas noches', 'Buenas tardes', 'Saludos']  # Definimos la Lista 1
lista2 = ['Adios', 'Buenos dias', 'Saludos']  # Definimos la Lista 2
print(superposicio(lista1, lista2))  # Mostramos la funcion, pasandole los parametros que necesitamos
