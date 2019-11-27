dicc = {}  # Definimos un diccionario
phrase = str(input("Introduce una frase: "))  # Pedimos un valor en formato texto
wrds = phrase.split()  # Creamos una lista donde se almacenarán todas las palabras de la variable anterior
'''Este bucle lo que hara es pasar por todas las posiciones de la lista segun su longitud'''
for i in range(len(wrds)):  # Iniciamos bucle
    '''Asigna la palabra en posicion i en la clave y la  lognitud de la palabra i en el valor segun su longitud'''
    dicc[wrds[i]] = len(wrds[i])
print(dicc)  # Mostramos el diccionario
