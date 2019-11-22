dicc = {}  # Definimos un diccionario
phrase = str(input("Introduce una frase: "))  # Pedimos un valor en formato texto
wrds = phrase.split()  # Creamos una lista donde se almacenarán todas las palabras de la variable anterior
for i in range(len(wrds)):  
    dicc[wrds[i]] = len(wrds[i])
print(dicc)
