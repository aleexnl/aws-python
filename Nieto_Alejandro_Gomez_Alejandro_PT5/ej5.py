# Pedimos datos
totalhoras = float(input("Horas trabajadas a la semana: "))
price = float(input("Precio por hora del trabajador: "))

# Inciiamos condicion
# Comprobamos si se tiene que calcular con horas extras
if totalhoras > 35:
    # Restamos a las horas 35 para obterner las extras
    extras = totalhoras - 35
    # Calculamos el precio total
    print("Importe final: " + str((extras*price*1.5) + ((totalhoras-extras)*price)))
# Si no ha echo horas extra, se calcula
else:
    print("Importe final: " + str(totalhoras*price))