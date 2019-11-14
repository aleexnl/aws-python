# Almacenar en variables para posterior uso
# FLOAT para permitir decimales
# INT para permitir numeros enteros
cini = float(input("Introduce la capital inicial : "))
tint = int(input("Introduce la tasa de interes : "))
nyea = int(input("Introduce numero de años: "))
# Calculo formula
# CPAG = cini * (1 + tint/100) ^ nyea
print("Diners a pagar: ", cini*(1+tint/100)**nyea)
