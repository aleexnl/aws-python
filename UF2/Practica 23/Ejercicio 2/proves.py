from matematiques import operacions_basiques  # Importar el modulo del paquete.
from matematiques import operacions_basiques as ob  # Importar el modulo del paquete con alias.
# Importar funciones del modulo.
from matematiques.operacions_basiques import sum_numbers, sub_numbers, multi_numbers, div_numbers

# A)
a, b = 13, 3  # Definimos variable

print("Operands = ", a, b)  # Mostramos las variables
print("Suma = ", operacions_basiques.sum_numbers(a, b))  # Llamamos a la funcion
print("Resta = ", operacions_basiques.sub_numbers(a, b))  # Llamamos a la funcion
print("Muliplicacion = ", operacions_basiques.multi_numbers(a, b))  # Llamamos a la funcion
print("Division = ", operacions_basiques.div_numbers(a, b))  # Llamamos a la funcion

# B)


print("Operands = ", a, b)  # Mostramos las variables
print("Suma = ", ob.sum_numbers(a, b))  # Llamamos a la funcion
print("Resta = ", ob.sub_numbers(a, b))  # Llamamos a la funcion
print("Muliplicacion = ", ob.multi_numbers(a, b))  # Llamamos a la funcion
print("Division = ", ob.div_numbers(a, b))  # Llamamos a la funcion

# C)


print("Operands = ", a, b)  # Mostramos las variables
print("Suma = ", sum_numbers(a, b))  # Llamamos a la funcion
print("Resta = ", sub_numbers(a, b))  # Llamamos a la funcion
print("Muliplicacion = ", multi_numbers(a, b))  # Llamamos a la funcion
print("Division = ", div_numbers(a, b))  # Llamamos a la funcion
