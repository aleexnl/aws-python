data = []  # Iniciamos la variable de lista
qty = int(input("Introduce la cantidad de datos a introducir: "))  # Pedimos cantidad de datos a introducir.
while qty < 1:  # Bucle hasta que la cantidad de datos a introducir sea mayor que 0
    print("Introduce un numero mayor que 0")  # Mensaje de error
    qty = int(input("Introduce la cantidad de datos a introducir: "))  # Pedimos cantidad de datos a introducir.
'''Este bucle lo que hace es pedir tantas vec estos 3 datos como se ha introducido en el input anterior.
Ademas luego los guarda en una lista temporal y esta misma se añade a la lista, reseteandose la lista temporal cada
vez para crear un bucle de listas en listas perfecto.'''
for i in range(qty):  # Iniciamos bucle
    tmpdata = []  # Iniciamos/Reinciamos variable de lista
    name = str(input("\nIntroduce tu nombre: "))  # Pedimos datos
    sname = str(input("Introduce tu apellido: "))  # Pedimos datos
    iname = str(input("Introduce tu inicial del segundo nombre: "))  # Pedimos datos
    tmpdata.append(sname), tmpdata.append(name), tmpdata.append(iname)  # Añadimos datos en este orden a la lista temp
    data.append(tmpdata)  # Añadimos la lista temporal a la lista oficial.
print("\n")  # Espacio para que los prints queden bien
'''Este bucle lo que hara es imprimir los valores de la lista oficial de cada sublista.'''
for j in range(len(data)):  # Iniciamos bucle
    print(data[j][1], data[j][2], ".", data[j][0])  # Printamos los valores de la lista segun posicion
