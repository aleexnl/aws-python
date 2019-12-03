# Definir una funció superposicio() que tomi dos llistes i retorni true si tenen al menys 1 membre en comú o retorni
# false de lo contrari.


def superposicio(l1, l2):
    cont = 0
    for i in range(len(l1)):
        if l1[i] in l2:
            cont += 1
    if cont != 0:
        return "True"
    elif cont == 0:
        return "False"


lista1 = ['Hola', 'Adios', 'Buenos dias', 'Buenas noches', 'Buenas tardes', 'Saludos']
lista2 = ['Adios', 'Buenos dias', 'Saludos']
print(superposicio(lista1, lista2))
