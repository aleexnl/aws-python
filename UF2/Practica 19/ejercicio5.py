'''Definir un histograma procedimient() que tomi una llista de números enters i
imprimeixi un histograma en la pantalla.'''

#creamos una lista para almacenar los numeros que de el usuario.
lista = []
#definimos una funcion para que coja cada numero de la lista, y lo muestre con asteriscos.
def histograma(asteriscos):
    for num in asteriscos:#multiplicamos el numero de la lista por los asteriscos
        print("*" * num)
#Le pedimos al usauario 3 numeros para añadir a la lista.
for numeros in range(3):
    num = int(input('Introduce un numero:'))
    lista.append(num)
#Llamamos a la funcion y sustituimos los valores de la lista en ella.
histograma(lista)