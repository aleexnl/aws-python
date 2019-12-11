#definimos la funcion alfabetica.
def alfabetica(paraula):
    paraula.isalpha()#Si la palabra es una palabra alfabetica la funcion isalpha nos dara un valor true en caso contrario false.
    if paraula.isalpha() == True:#si el valor es True le diremos que es una palabra alfabetica y si no que no lo es.
        print('La paraula, es alfabetica')
    else:
        print('La paraula, es no alfabetica')

hola = input('Introduce una palabra:')#pedimos una palabra al usuario.
#sustituimos el argumento paraula por la variable hola en la funcion alfabetica.
alfabetica(hola)