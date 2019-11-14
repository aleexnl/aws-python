import math  # Importa la libreria math para hacer calculos

# APARTADO A
# Pide la base y la almacena como integreer
b = int(input("Escribe la base: "))
# Pide la altura y la almacena como integreer
h = int(input("Escribe la altura: "))
# Muestra un texto acompañado de
# el resultado de la formula del calculo
# L = (2*b) + (2*h)
print("El perimetro del rectangulo es: ", (2*b)+(2*h))
# Imprime texto acompañado de la formula
# S = b*h
print("El perimetro del rectangulo es: ", b*h)

# APARTADO B
# Pide el radio y lo almacena como integreer
r = int(input("Escribe el radio: "))
# Imprime un texto acompañado de la formula
# A = πr^2
# Utilizamos el math.pi para referirnos al simbolo π libreria math
print("El area del circulo es : ", end="")
# El end nos permite añadir el siguiente print como continuacion.
# El format nos permite imprimir solo 2 decimales
print("{0:.2f}".format(math.pi*r**2))
# Imprime un texto acompañado de la formula
# A = πr2
print("El area del circulo es : ", end="")
print("{0:.2f}".format(2*math.pi*r))

# APARTADO C
# Pide el radio y lo almacena como integreer
resf = int(input("Escribe el radio: "))
# Imprime un texto acompañado de la formula
# V =4/3πr^3
# Utilizamos el math.pi para referirnos al simbolo π libreria math
print("El volumen de la esfera es : ", end="")
# El end nos permite añadir el siguiente print como continuacion.
# El format nos permite imprimir solo 2 decimales
print("{0:.2f}".format(int(4*math.pi*(resf**3))/3))
