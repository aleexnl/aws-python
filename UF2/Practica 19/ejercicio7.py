#creamos una lista
lista = [1,2,3,4]
#definimos la funcion de suma en la cual va a coger los numeros que hay en lista y los va a ir sumando dentro de suma.
def sum(numeros):
    suma = 0
    for i in numeros:
        suma = suma + i
    return suma
#definimos la funcion de multiplicacion en la cual va a coger los numeros que hay en la lista y los va a ir multiplicando dentro de multiplicacio.
def multip(numeros):
    multiplicacio = 1
    for i in numeros:
        multiplicacio = multiplicacio * i
    return multiplicacio
#ahora vamos a imprimir las dos funciones sustituyendo los valores por los que hay dentro de lista.
print(sum(lista))
print(multip(lista))
