lista = []  # Iniciamos lista
indice = 0  # Iniciamos contador de letras
mayusculas = 0  # Iniciamos contador de mayusculas
continuar = "S"  # Iniciamos un "Bool"
'''Este bucle pedira palabras y las metera dentro de la lista hasta que se le indique que ya no prosiga
con el bucle mediante un texto que se repite al introducir una palabra.'''
while continuar != "N":
    lista.append(str(input("Introduce una palabra: ")))
    continuar = str(input("Continuar? (S/N)")).upper()
'''Este bucle for tiene un while anidado. El for lo que hace es ir pasando por todas las posiciones de la lista;
en otras palabras pasará por cada palabra de la lista'''
for i in range(len(lista)):
    indice = 0
    '''El while lo que hara es, pasar letra por letra de la palabra que se esta analizando actualmente y comprobar si es
mayuscula. Si es mayuscula la sumara a un contador total.'''
    while indice < len(lista[i]):
        letra = lista[i][indice]
        if letra.isupper() is True:
            mayusculas += 1
        indice += 1
print("Total mayusculas: ", mayusculas)  # Imprime total de maysuculas
