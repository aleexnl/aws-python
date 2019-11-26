lista = [('Hola', 'Don pepito'), ('Hola', 'Don Jose'), ('Bon', 'Dia')]
diccionario = {}
for i in lista:
    if i[0] not in diccionario:
        diccionario[i[0]] = []
    diccionario[i[0]].append(i[1])

print(diccionario)