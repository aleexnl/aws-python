# Pedimos año
year = int(input("Introduce un año: "))
# Comprobamos que sean las condiciones de año bisiesto
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Es bisiesto")
# Si no es devuelve negación
else:
    print("No es bisiesto")
