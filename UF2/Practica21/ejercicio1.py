#definimos la funcion tres lineas y le asignamos un valor al argumento de la funcion.
def tres_linies(blanco = 3):
    for i in range(blanco):#Decimos que en el rango de blanco pinte un espacio en blanco.
        print(' ')
#definimos la funcion nueve lineas y le asignamos un valor al argumento de la funcion.
def nou_linies(veces= 3):
    for i in range(veces):#decimos que en el rango de veces pinte la funcion tres_lineas
        tres_linies()
#definimos la funcion limpiar pantalla.
def neteja_pantalla(lineas = 25):
    for i in range(lineas):#decimos que para i en un rango de lineas que es 25, imprima una linea en blanco
        print(' ')
#definimos la funcion concatena n vegadas.
def concatena_n_vegades(c,n):
    for i in range(n):#Vamos a imprimir c las veces que es n
        print(c)
#Llamamos a las funciones
tres_linies()
nou_linies()
concatena_n_vegades('hola',5)
neteja_pantalla()
'''si movemos la llamada a esta funcion al principio del codigo
nos aparecera un mensaje de error como que el nombre neteja_pantalla no esta definidop'''
