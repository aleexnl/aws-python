""" Feu una funció “calculaResidu” a la que passem per paràmetre el dividend i el divisor, i torna com a resultat el
residu de la divisió. calculaResidu( dividend,divisor) """


def calcularesidu(dividend, divisor):
    res = dividend % divisor
    return res


divend = float(input('Introduce el dividend: '))
divsor = float(input('Introduce el divisor: '))
while divend and divsor == 0:
    print('¡No se puede dividir entre cero!')
    divend = float(input('Introduce el dividend: '))
    divsor = float(input('Introduce el divisor: '))
total = calcularesidu(divend, divsor)
print('El residuo es: ', total)
