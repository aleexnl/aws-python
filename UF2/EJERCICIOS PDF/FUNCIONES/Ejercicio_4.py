"""Creeu una funció “lecturaInterval” que faci una lectura d’una xifra dins d’un interval. A la funció li passarem el
valor mínim del rang, el valor màxim, i ens tornarà un valor llegit del teclat que estigui dins d’aquest rang. Com a
l’exercici anterior, fins que el nombre no estigui dins l’interval, la funció continuaràdemanat el nombre a l’usuari."""


def lecturainterval(minnum, maxnum):
    print('Introduce un numero en el rango de ', minnum, ' a ', maxnum, end='')
    num = int(input(' : '))
    while num not in range(minnum, maxnum + 1):
        print('¡No esta en el rango!')
        print('Introduce un numero en el rango de ', minnum, ' a ', maxnum, end='')
        num = int(input(' : '))


num1 = int(input('Introduce el numero minimo: '))
num2 = int(input('Introduce el numero maximo: '))
lecturainterval(num1, num2)
