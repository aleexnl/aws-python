# Escriu un programa que tingui una funció que demani dos anys i retorni quants anys de traspàs hi ha entre
# les dos dates (inclosos els dos anys):


def anostraspaso():  # Iniciamos la funcion
    cont = 0  # Iniciamos el contador de años de traspaso
    year1 = int(input("Introduce el primer año: "))  # Pedimos el año nº1
    year2 = int(input("Introduce el segundo año: "))  # Pedimos el año nº2
    """ Este bucle lo que hace es comprobar que el segundo año sea mayor que el primero. De lo contrario estara
     pidiendo los valores hasta que se cumpla la condicion del bucle"""
    while year2 <= year1:  # Iniciamos bucle
        print(year2, " no es mayor que ", year1)  # Mostramos error
        year1 = int(input("Introduce el primer año: "))  # Pedimos el año nº1
        year2 = int(input("Introduce el segundo año: "))  # Pedimos el año nº2
    """ Este bucle lo que hace es ir pasando entre los años que hay de diferencia con estos includios, comprobando
     si son años de traspaso o no. Si lo son les suma uno al contador de años de traspaso y si no continua sin 
     hacer nada"""
    for year in range(year1, year2 + 1):  # Iniciamos un bucle iterativo
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:  # Condicional que comprueba si es año de traspaso
            cont += 1  # Suma uno al contador de años de traspaso
    print("De el año ", year1, " al año ", year2, " hay ", cont, " años de traspaso y ", (year2 - year1) + 1,
          " años de diferencia.")
    # Printa el mensaje personalizado mostrando los años, los años de traspaso y la diferencia entre los dos años


anostraspaso()  # Llamamos a la funion
