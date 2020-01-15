from modules import functions as fc # Importamos la funcion que hemos creado.

number_list = [] # Creamos una lista.
print("INTRODUCE UN NUMERO NEGATIVO PARA ACABAR")
''' Creamos un bucle infinito del cual no vamos a poder salir hasta que introducimos un numero negativo, mientras los
numeros positivos se van a ir añadiendo a la lista'''
while True:
    try:
        number = int(input("Introduce un numero: "))
        if number >= 0:
            number_list.append(number)
        elif number < 0:
            break
    except ValueError: # Si introducimos un numero decimal nos mostrara el siguiente mensaje de error.
        print("ERROR: Introduce solo valores enteros")

print(fc.recursive_sum(number_list, 0)) # Llamamos a la funcion y sustituimos su valor por la lista.
