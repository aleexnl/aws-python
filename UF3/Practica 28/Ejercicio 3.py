#creamos una lista para la informaicon que queramos separar con delimitador
lista = ["nombre", "fecha", "horas", "signatura"]
# Creamos una variable "archivo" para abrir el arahcivo con txt y ponemos "r" que
# significa modo lectura
archivo = open("ejercicio.txt","r")
# Creamos una variable "delimitador", que nos sirvira separar la informacion del
# archivo y de la lista mediante dos puntos
delimitador = " : "
# Creamos una variable contador para leer todas las lineas del arhivo con readline
contador = len(archivo.readline())
# seek sirve para situar en punto inicio mostrando en la posicion 0
archivo.seek(0)
# Con este bucle pasaremos por toda la informacion
for i in range(1, contador-1):
# Finalmente printamos en la pantalla la información de la lista separado con el
# delimitador junto con las lineas del archivo.
    print(lista[i-1], delimitador, archivo.readline())
# Finalmente cerramos el archivo
archivo.close()


