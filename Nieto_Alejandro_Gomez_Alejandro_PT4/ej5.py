# (F − 32) × 5/9
f = float(input("Introduce los grados Fahrenheit: "))
# .format para imprimir solo 2 decimales
print("{0:.2f}".format(float((f-32)*5/9)), "Grados Celsius")
