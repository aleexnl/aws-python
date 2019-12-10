def alfabetica(paraula):
    paraula.isalpha()
    if paraula.isalpha() == True:
        print('La paraula, es alfabetica')
    else:
        print('La paraula, es no alfabetica')

hola = input('Introduce una palabra:')
alfabetica(hola)