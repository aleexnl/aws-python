#creamos una lista
lista = [1,2,3,4]
#definimos la funcion de suma en la cual va a coger los numeros que hay en lista y los va a ir sumando dentro de suma.
def sum(numeros):
    suma = 0#declaramos una variable suma
    for i in numeros:#por cada numero en numeros
        suma = suma + i#lo sumamos a suma
    return suma
#definimos la funcion de multiplicacion en la cual va a coger los numeros que hay en la lista y los va a ir multiplicando dentro de multiplicacio.
def multip(numeros):
    multiplicacio = 1#declaramos una variable muktiplicacion con valor 1
    for i in numeros:#por cada numero dentro de numeros
        multiplicacio = multiplicacio * i #lo multiplicamos por multiplicacio y lo guardamos
    return multiplicacio
#ahora vamos a imprimir las dos funciones sustituyendo los valores por los que hay dentro de lista.
print(sum(lista))
print(multip(lista))
