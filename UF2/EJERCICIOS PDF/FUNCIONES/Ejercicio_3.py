"""Creeu una funció “llegeix1a10” que s’encarregui de demanar a l’usuari que introdueixi pel teclat un nombreentre 0 i
10. Fins que el nombre no està entre el 0 i el 10, continuademanat a l’usuari el número. La funció no té paràmetres, i
retorna un nombre sencer, que és el que s’ha llegit a la funció."""


def llegeix1a10():
    num = int(input("Introduce un numero del 0 al 10: "))
    while num not in range(0, 11):
        print('¡No esta en el rango especificado!')
        num = int(input("Introduce un numero del 0 al 10: "))


llegeix1a10()
