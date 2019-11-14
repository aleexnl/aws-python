# Pedimos edad
age = int(input("Introduce tu edad: "))
# Pedimos carnet
idask = str(input("¿Tienes carnet de estudiante?: "))
# Entramos en condicional para ver si es menor
if age < 10:
    # Opcion de menor de 3
    if age < 3:
        # Tiene carnet
        if idask == "S" or idask == "s":
            # Calculo precio
            pvp = 2 - (0.1 * 2)
            print("Precio: ", pvp, "€")
        # No tiene carnet
        else:
            print("El precio es de 2€")
    # Opcion de menor de 10
    elif age < 10:
        # Tiene carnet
        if idask == "S" or idask == "s":
            # Calculo precio
            pvp = 10 - (0.1 * 10)
            print("Precio: ", pvp, "€")
        # No tiene carnet
        else:
            print("El precio es de 10€")
# Mayor de 10
elif age >= 10:
    # Tiene carnet
    if idask == "S" or idask == "s":
        # Calculo descuento
        pvp = 25 - (0.1 * 25)
        print("Precio: ", pvp, "€")
    # No tiene carnet
    else:
        print("El precio es de 25€")
# Datos no bien introducidos
else:
    print("Error no especificado")
