# Pedir información
num1 = int(input("Introduce el 1r numero: "))
num2 = int(input("Introduce el 2o numero: "))
num3 = int(input("Introduce el 3r numero: "))
# Comprobamos que num1 sea menor que num2
if num1 < num2:
    # Comprobamos que num2 sea menor que num3
    if num2 < num3:
        # Si se cumple la condicion
        print("Estan ordenados")
    else:
        # No se cumple
        print("No estan ordenados")
# No se cumple
else:
    print("No estan ordenados")
