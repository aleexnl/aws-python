# Precio hora
constant_ph = 30
# Precio metro cable
constant_pm = 0.5
# Pedimos las horas trabajadas
ht = float(input("Horas trabajadas: "))
# Pedimos los metros instalados
mi = float(input("Metros instalados: "))

# Calculo de el precio total metros cable
pmt = mi*constant_pm
# Calculo precio total + IVA
pmtiva = pmt+(pmt*0.21)

# Mostrar la información
print("Precio bruto: ", pmt)
print("Precio con IVA: ", pmtiva)
