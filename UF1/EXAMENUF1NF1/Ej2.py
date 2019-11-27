h = int(input("Introduce la altura: "))  # Pedimos valores
long = int(input("Introduce la longitud: "))
while h < 4 or long < 4:  # Comprobamos que no sean erroneos
    print("¡Introduce valores validos partiendo de 4!")  # Si lo son mostrar error
    if h < 4:  # Comprobar si altura es erroneo
        h = int(input("Introduce la altura: "))  # Volver a pedir
    elif long < 4:  # Comprobar si longitud es erroneo
        long = int(input("Introduce la longitud: "))  # Volver a pedir
