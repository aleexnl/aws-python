# Pedimos edad
age = int(input("Introduce tu edad: "))
# Entramos en condicional para ver si es menor
if age < 10:
    # Opcion de menor de 3
    if age < 3:
        print("El precio es de 2€")
    # Opcion de menor de 10
    elif age < 10:
        print("El precio es de 10€")
# Cualquier otra dead
else:
    print("El precio es de 25€")
