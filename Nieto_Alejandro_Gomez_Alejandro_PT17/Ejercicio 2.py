import random

''' EJERCICIO 2'''

''' Definimos las variables '''
frase = " On the border line and of the edge and where I walk alone "  # En esta ponemos la frase
palabraslist = frase.split()  # Aqui lo que hacemos es una lista con las palabras de la frase separadas
diccionario = dict.fromkeys(palabraslist)  # Y aqui convertimos la lista creada anteriormente a claves en un diccionario

''' Hacemos un bucle en el cual diremos que vaya recorriendo las palabras de la lista y en la clave del diccionario 
que tenga ese nombre añadiremos las veces que aparece en la frase con un count a la lista creada con las palabras'''
for i in palabraslist:
    diccionario[i] = palabraslist.count(i)
print(diccionario)  # Finalmente lo printamos

''' EJERCICIO 2.3'''

''' Iniciamos un diccionario y una lista '''
diccionario2 = {}
lista = []
''' En este for lo que hacemos es una lista con todas las letras de la frase para transformarlo en claves despues'''
for i in frase.lower():
    if i != ' ':
        lista.append(i)

''' Aqui es cuando hacemos la conversion indicada anteriormente '''
diccionario2 = dict.fromkeys(lista)

''' Y por ultimo hacemos lo mismo que en el ejercicio 2 para que se vayan añadiendo a cada clave su valor
(en este caso es el numero de veces que aparece esa letra en la frase )'''
for b in diccionario2:
    diccionario2[b] = lista.count(b)
print(diccionario2)  # Y por ultimo lo printamos

''' EJERCICIO 2.4'''
dicc = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}  # Iniciamos lista con todos los valores
opc = int(input("¿Cuantas veces quieres tirar los dados? "))  # Pedimos cuantas veces tiramos los dados
'''Este bucle pedira el valor hasta que sea mayor que 0'''
while opc < 1:  # Comprobamos que el valor sea mayor que 1
    print("¡Introduce un valor mayor que 0!")  # Mostramos error
    opc = int(input("¿Cuantas veces quieres tirar los dados? "))  # Pedimos valor
'''Este bucle lo que hara es repetir tantas veces su contenido como se ha especificado en el anterior input'''
for i in range(opc):  # Iniciamos bucle
    dice1 = random.randint(1, 6)  # Variable 1 con un valor random del 1 al 6
    dice2 = random.randint(1, 6)  # Variable 2 con un valor random del 1 al 6
    dicc[dice1] += 1  # Sumamos el valor de el numero que ha salido 1
    dicc[dice2] += 1  # Sumamos el valor de el numero que ha salido 1
print(dicc)  # Mostramos diccionario final
