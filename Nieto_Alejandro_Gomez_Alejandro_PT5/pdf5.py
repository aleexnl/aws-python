# Pedimos 3 numeros
num1 = float(input("Introduce el 1r numero: "))
num2 = float(input("Introduce el 2o numero: "))
num3 = float(input("Introduce el 3r numero: "))
# Entramos en condicional
# Num1 mayor que num2
if num1 > num2:
    # Num1 mayor que num3
    if num1 > num3:
        print("El numero mas grande es: ", num1)
    # Entonces num2 mayor que num3
    elif num2 > num3:
        print("El numero mas grande es: ", num2)
    #
    else:
        print("El numero mas grande es: ", num3)
elif num2 > num3:
    print("El numero mas grande es: ", num2)
else:
    print("El numero mas grande es: ", num3)
