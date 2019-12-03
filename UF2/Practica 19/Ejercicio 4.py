# Definir una funció superposicio() que tomi dos llistes i retorni true si tenen al menys 1 membre en comú o retorni
# false de lo contrari.


def superposicio(l1, l2):
    for i in range(len([l1])):
        for j in range(l1[i]):
            if l1[i][j] in l2:
                return True


lista1 = ['Hola', 'Adios', 'Buenos dias', 'Buenas noches', 'Buenas tardes', 'Saludos']
lista2 = ['Adios', 'Buenos dias', 'Saludos']
print(superposicio(lista1, lista2))
