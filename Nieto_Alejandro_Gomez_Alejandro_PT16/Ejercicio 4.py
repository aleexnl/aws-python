''' Primero pediremos la cantidad de articulos que queremos introducir/configurar'''
x = int(input("Cuantis articulos quereis introducir/configurar\n"))
d = {} # Creamos un diccionario vacio
''' Preguntamos al usuario los diferentes datos que necesitamos y los guradamos en una variable'''
for i in range(x):
    print("Introduce los datos del articulo", i+1)
    num = int(input("Numero de referencia: "))
    nombre = input("Nombre del articulo: ")
    precio = int(input("Precio: "))
    cantidad = int(input("Cantidad en el almacen: "))
    d[i+1] = [num, nombre, precio, cantidad]

''' Iniciamos un bucle infinito '''
while True:
    ''' Printaremos el menu dandole a escojer una opcion al usuario'''
    print("Introduce una de las opciones (A, B, C o F)")
    print("MENU PRINCIPAL", "\nA) Lista de articulos", "\nB) Modificar articulos",
          "\nC) Buscar articulos por el numero de "
          "referencia", "\nF) Fi")
    opcion = input("Que opcion quieres escoger\n")
    ''' Si elijen la opcion A printara la lista con todos los articulos introducidos'''
    if opcion == "A":
        ''' Los dos prints estos serian lo que viene a ser los nombres de las tablas de la lista de articulos que vamos a mostrar '''
        print("Lista de articulos")
        print("Num. referencia".ljust(20), "Nombre".ljust(5), "Precio".ljust(10), "Cantidad".ljust(10))
        ''' Este bucle de aqui lo que hace es que vaya mostrando todos los articulos que hay en orden'''
        for i in d:
            print(str(d[i][0]).ljust(20), str(d[i][1]).ljust(5), str(d[i][2]).ljust(10), str(d[i][3]).ljust(10))

        input("Dale a cualquier tecla para volver al menu principal")# Hacemos que vuelva a salir el menu

    elif opcion == "B": # Si la opcion es B
        ''' Mostramos los articulos que se pueden modificar con un bucle'''
        for i in d:
            print("#", i, "#", d[i][0], d[i][1])

        z = int(input("Que articulo quieres modificar?: \n")) # Pedimos al usuario que elija el articulo que quiere modficiar
        if z not in d: # Sis e equivoca se lo diremos y volveremos al bucle inicial
            print("Este elemento no esta en el diccionario")

        else: # Si no pone un numero erroneo podra empezar a modificar el articulo
            numrefnuevo = int(input("Introduce numero de referencia\n"))
            nombrenuevo = input("Introduce nombre\n")
            precionuevo = int(input("Introduce el precio\n"))
            cantidadnueva = int(input("Introduce cantidad en el almacen\n"))
            d[z][0] = numrefnuevo
            d[z][1] = nombrenuevo
            d[z][2] = precionuevo
            d[z][3] = cantidadnueva

        input("Dale a cualquier tecla para volver al menu principal") # Hacemos que vuelva a salir el menu
    elif opcion == "C": # Si la opcion es C
        refbusc = int(input("Introduce el numero de referencia a buscar")) #Preguntamos el numero que queremos buscar
        encontrado = 0
        p = 0
        ''' Miraremos si existe algun articulo con ese numero de referencia'''
        for i in d:
            if refbusc == d[i][0]:
                encontrado = 1
                p = i
                break
        if encontrado == 1: # Si lo hay lo printamos
            print(d[p])
        else: # Sino decimos que no hay
            print("No se ha encontrado")

        input("Dale a cualquier tecla para volver al menu principal")# Hacemos que vuelva a salir el menu

    elif opcion == "F": # Por ultimo si la respuesta es F saldremos del programa
        break
    else: # Este else lo ponemos mas que nada por si el usuario se equivoca de opcion y pone alguna no valida
        print("Opcion no correcta")

