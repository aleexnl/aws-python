# Imprimimos el menu
# .format para tener ordenado el menu
print("==============================")
print('{0:1} -'.format("1."), end=" ")
print("Euros a Dolars".rjust(1))

print('{0:1} -'.format("2."), end=" ")
print("Euros a Yens".rjust(1))

print('{0:1} -'.format("3."), end=" ")
print("Dolars a Euros".rjust(1))

print('{0:1} -'.format("4."), end=" ")
print("Dolars a Yens".rjust(1))

print('{0:1} -'.format("5."), end=" ")
print("Yens a Euros".rjust(1))

print('{0:1} -'.format("6."), end=" ")
print("Yens a Dolars".rjust(1))

print("==============================")
# Preguntamos la opcion
opc = int(input("Escoje una opción: "))
print("==============================")
# Iniciamos las condiciones,
# si se cumple alguna printa,
# si no suelta error

if opc == 1:
    eur = float(input("Introduce cantidad a convertir: "))
    print("Euros a Dolars: ", eur * 1.11894)
elif opc == 2:
    eur = float(input("Introduce cantidad a convertir: "))
    print("Euros a Yens: ", eur * 115.998)
elif opc == 3:
    eur = float(input("Introduce cantidad a convertir: "))
    print("Dolars a Euros: ", eur / 1.11894)
elif opc == 4:
    eur = float(input("Introduce cantidad a convertir: "))
    print("Dolars a Yens: ", (eur / 1.11894) * 115.998)
elif opc == 5:
    eur = float(input("Introduce cantidad a convertir: "))
    print("Yens a Euros: ", eur / 115.998)
elif opc == 6:
    eur = float(input("Introduce cantidad a convertir: "))
    print("Yens a Dolars: ", (eur / 115.998) * 1.11894)
else:
    print("¡Introduce una opcion valida!")
