word1 = str(input("Introduce la palabra 1 :"))  # Pedimos la primera palabra
word2 = str(input("Introduce la palabra 2 :"))  # Pedimos la segunda palabra
list = [[], []]  # Iniciamos variable de almacenaje 1
'''Iniciamos bucle que apendara todas las letras de la palabra en una lista'''
for i in word1:  # iniciamos bucle
    list[0].append(i.lower())  # añadimos la letra a la lista
'''Iniciamos bucle que apendara todas las letras de la palabra en una lista'''
for i in word2:  # iniciamos bucle
    list[1].append(i.lower())  # añadimos la letra a la lista
'''Este es un condicional sencillo. Si se cumplen todas mostrara que riman, si solo se cumplen dos mostrara que 
riman poco y si solo se cumple una dira que no riman.
Este se basa siempre en las 3 ultimas posiciones de las listas creadas anteriormente.'''
if list[0][-1] in list[1][-1]:
    if list[0][-2] in list[1][-2]:
        if list[0][-3] in list[1][-3]:
            print("Las palabras ", word1, " y ", word2, " riman.")  # Muestra mensaje
        elif list[0][-3] not in list[1][-3]:
            print("Las palabras ", word1, " y ", word2, " riman poc.")  # Muestra mensaje
    elif list[0][-2] not in list[1][-2]:
        print("Las palabras ", word1, " y ", word2, " no riman.")  # Muestra mensaje
