lst = [2.3, 5.6, 7.2, 5.0, 3.0, 2.1]  # Creamos la lista

# A) Mostrar la lista por pantalla
print("Lista original: ", lst)

# B) Invertir la lista y mostrar por pantalla
lst.reverse()  # Funcion que nos permite invertir la lista
print("\nLista invertida: ", lst)
lst.reverse()  # Devolvemos la lista a su estado original

# C) Substituir 7.2 por un 6
lst[2] = 6  # Asignar valor a la posicion de la lista (la primera posicion siempre es 0)
print("\nLista con valor substituido: ", lst)

# D) Leer numero del teclado y guardarlo en el 4º numero
print("\n")
num = float(input("Introduce un numero entero: "))  # Pedir un valor Float
lst[3] = num  # Asignar valor a la posicion de la lista mediante una variable
print(lst)

# E) Mostrar las posiciones pares de la lista
print("\nNUMEROS EN POSICIONES PARES: ", end="")  # Mostramos mensaje
'''Este bucle lo que hara es pasar por todas las posiciones de la lista segun su largo y, si el valor de la posicion
se puede dividir entre cero lo mostrara.'''
for i in range(len(lst)):
    if i % 2 == 0:
        print(lst[i], end="\t")

# F) Mostrar las posiciones impares de la lista
print("\n")
print("\nNUMEROS EN POSICIONES IMPARES: ", end="")
'''Este bucle lo que hara es pasar por todas las posiciones de la lista segun su largo y, si el valor de la posicion
no se puede dividir entre cero lo mostrara.'''
for i in range(len(lst)):
    if i % 2 != 0:
        print(lst[i], end="\t")
