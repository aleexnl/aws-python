# DEFINICION DE VARIABLES
customers = [['444B', 200, 70, 40, 120], ['333A', 200, 35, 50], ['555C', 100, 30, 23, 30, 60, 1000]]
# FIN DEFINICION VARIABLES
'''Este bucle estara en marcha hasta que el usuario presione X'''
while True:  # Iniciamos bucle
    # DEFINICION VARIABLES RESETEABLES
    consumo = 0
    dforta = []
    pconsumo = []
    # FIN DEFINICION VARIABLES RESETEABLES
    # MOSTRAR MENU
    print("\n")
    print("MENU PRINCIPAL: ")
    print("Opcion 1: \tConsum total")
    print("Opcion 2: \tDespesa forta")
    print("Opcion 3: \tPrimer gastador")
    print("Opcion 4: \tAñadir cliente")
    print("X per finalizar")
    print("\n")
    # FIN MOSTRAR MENU
    opc = str(input("Introduce una opcion: ")).upper()  # Pedimos una opcion para interactuar
    if opc == '1':  # Si la opcion es uno
        print("Consumo total de los clientes: ", end="")  # Muestra mensaje personaliado
        '''Un bucle que ira por cada posicion de la lista sumando su contenido'''
        for i in range(len(customers)):  # Iniciamos bucle
            consumo += sum(customers[i][2:])  # Sumamos cada numero a partir de la posicion 2 (evitar id + tarifa)
        print(consumo)  # Mostramos calculo total
    if opc == '2':  # Si la opcion es 2
        maxconsumo = int(input("Introduce un limite de consumo: "))  # Pedimos el consumo que queremos de limite
        '''Un bucle que pasara por todo el contenido de las listas que hay buscando un numero igual o mayor al
        introducido. Si aparece se añade a la lista para luego mostrarlos, y, si ya esta añadidio, no se duplica el
        valor'''
        for j in range(len(customers)):  # Iniciamos bucle segun longitud de lista
            for k in range(2, len(customers[j])):  # Iniciamos bucle segun longitud de la posicion de la lista
                if customers[j][k] >= maxconsumo:  # Si la condicion se cumple
                    if customers[j][0] not in dforta:  # I esta se cumple
                        dforta.append(customers[j][0])  # Añade contenido a la lista
        dforta.sort()  # Ordenamos la lista
        print(dforta)  # Mostramos la lista ordenada
    if opc == '3':  # Opcion 3
        maxconsumo = int(input("Introduce un limite de consumo: "))  # Pedimos valor
        '''Este bucle tiene la misma mecanica que el anterior; ira por todo el contenido total de la lista. Lo unico que
        cambia es que una vez ha encontrado un valor se para el bucle'''
        for j in range(len(customers)):  # Iniciamos bucle segun longitud total de lista
            for k in range(2, len(customers[j])):  # Iniciamos bucle segun longitud total de la lista segun j
                if customers[j][k] >= maxconsumo:  # Si es mayor que el valor
                    if len(pconsumo) == 0:  # I la lista esta vacia
                        pconsumo.append(customers[j][0])  # Añade el valor
                    if len(pconsumo) != 0:  # Si la lista no esta vacia rompe este bucle
                        break  # Romper bucle
                if len(pconsumo) != 0:  # Si la lista no esta vacia rompe este bucle
                    break  # Romper bucle
        print(pconsumo)  # Mostramos la lista
    if opc == '4':  # Opcion 4
        temp = str(input("Introduce el codigo de cliente: ")).upper()  # Pedimos el codigo del cliente
        while len(temp) != 4:  # Si la longitud no es correcta se inicia bucle
            print("¡Introduce un codigo de 4 caracteres!")  # Muestra error
            temp = str(input("Introduce el codigo de cliente: ")).upper()  # Pide valor
        customers.append([temp])  # Añadimos el codigo
        temp = int(input("Introduce la tarifa del cliente: "))  # Pedimos la tarifa
        while temp < 1:  # Si el valor no es correcto se inicia bucle
            print("¡Un valor mayor a 0!")  # Mensaje de error
            temp = int(input("Introduce la tarifa del cliente: "))  # pedimos la tarifa
        customers[-1].append(temp)  # Se añade la tarifa basandose en el ultimo valor añadido
        temp = int(input("Cuantos consumos tiene ?"))  # Pedimos consumos
        if temp > 0:  # si tiene consumos
            '''Este es un bucle sencillo que pedira y añadira a la lista tantos valores como se han especificado
            en el input anterior'''
            for i in range(temp):  # Iniciamos bucle
                print("Consumo Nº: ", i+1)  # Mostramos mensaje personalizado
                temp1 = int(input("Introduce el consumo"))  # Pedimos consumo
                customers[-1].append(temp1)  # Añadimos el valor basandose en el ultimo valor añadido
        print(customers)  # Mostramos la lista
    if opc == 'X':  # Si la opcion del menu es X
        break  # Finaliza el programa
