""" Definiu i programeu una funció que, donats un preu i un percentatge de descompte, ens torni el preu amb el descompte
 aplicat. La funció té dos paràmetres: preu i percentatge. Retorna el preu amb el descompteaplicat. """


def descompte(a, b):
    disc = 1 - (b / 100)
    totalprice = a - (a - (a * disc))
    return totalprice


price = float(input('Introduce el precio: '))
discount = int(input('Introduce el descuento: '))
total = descompte(price, discount)
print('Precio total: ', total, '€')
