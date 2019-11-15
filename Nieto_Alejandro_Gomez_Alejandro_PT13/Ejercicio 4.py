lst = []  # Iniciamos la lista.
factory = []
total = 0   # Iniciamos variable a zero.
# Pedimos cantidad de nums a anadir en la lista.
qty = int(input("Introduce la cantidad de numeros ENTEROS a anadir en la lista: "))
while qty < 1:  # Comprobamos que sea un valor valido
    print("Introduce un valor mayor que 0")  # Mostramos error
    qty = int(input("Introduce la cantidad de numeros ENTEROS a anadir en la lista: "))
'''Este bucle lo que hara es pedir y anadir a la lista tantos numeros como se han indicado en el input anterior.'''
for i in range(qty):  # Iniciamos bucle
    num = int(input("Introduce un numero ENTERO a añadir: "))  # Pedimos valor
    while num < 0:  # Comprobamos que sea un valor valido
        print("Introduce un numero mayor o igualque 0")  # Mostramos error
        num = int(input("Introduce un numero ENTERO a añadir: "))  # Pedimos valor
    lst.append(num)  # Añadimos valor a la lista
print("Numeros introducidos: ", lst)  # Mostramos la lista de valores
'''Este bucle lo que hara es sumar a una variable la suma total de todos los numeros que hay en la lista,
pasando por todas las posiciones de la lista hasta llegar hasta el final'''
for j in range(len(lst)):  # Iniciamos el bucle
    total += lst[j]  # Hacemos la suma de VALOR + NUM.POSICION LISTA
print("Suma de todos los valores: ", total)  # Mostramos el total de la suma
print("Media de los valores: ", total / len(lst))  # Hacemos el calculo de la media y lo mostramos
'''Este bucle hara el factorial de cada numero y lo apendara una lista, de tal manera que cuando acabe el bucle este lo
que hara es mostrar todos los factoriales de cada numero.'''
for k in range(len(lst)):
    factorynum = [lst[k]]
    timer = lst[k]
    for l in range(lst[k]):
        if timer - 1 == 0:
            break
        factorynum[0] = factorynum[0] * (timer - 1)
        timer -= 1
    factory.append(factorynum[0])
print("Factoriales de cada numero: ", factory)

'''ESTA PARTE DE CODIGO HACE LA DESCOMPOSICION FACTORIAL DE CADA NUMERO EN LA LISTA Y LUEGO AL MUESTRA. NO FUNCIONA CON
EL 0, 1 Y 3'''
# factory = []
# for k in range(len(lst)):  # Iniciamos el bucle
#     factory = []  # Iniciamos la lista de factoriales
#     dvsr = 2  # Iniciamos el numero divisor inicial
#     while True:  # Iniciamos un bucle anidado
#         if lst[k] % dvsr == 0:  # Si el numero es divisor...
#             factory.append(dvsr)  # Añade el numero a la lista
#             lst[k] = lst[k] / dvsr  # Cambia el valor de la lista
#         if lst[k] % dvsr != 0:  # Si no es divisor...
#             dvsr += 1  # Cambiamos directamente el valor de i
#         if lst[k] == dvsr:  # Si el divisor es igual que el numero
#             factory.append(dvsr)  # Lo añade a la lista
#             break # Paramos el bucle anidado
#     print("Descomposicion factorial :", factory)  # Mostramos la lista de la descompsoicion factorial de el numero

