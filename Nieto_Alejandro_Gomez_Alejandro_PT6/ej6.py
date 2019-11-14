# Pedimos valor
qty = int(input("Cuantos numeros vas a introducir: "))
print("\n")
# Iniciamos variables
aritnum = 0
maxnum = 0
minnum = 0

# Iniciamos bucle:
# Se hará tantas veces como numeros se han pedido
for i in range(qty):
    num = float(input("Introduce el numero: "))
    # Compara si es mayor que el numero mayor actual
    if num > maxnum:
        maxnum = num
    # Compara si es menor
    elif num < minnum:
        minnum = num
    # Lo suma para la arimetica
    aritnum = aritnum + num
# Calcula la aritmetica
aritnum = aritnum / qty
print("\n")
# Printa resultados
print("Numero mayor: ", maxnum)
print("Numero menor: ", minnum)
print("Numero media: ", aritnum)
