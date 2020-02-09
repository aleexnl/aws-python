import os #Importamos el modulo os que nos permite usar las funcionalidades del sistema operativo.

def delNomFitxer(): # definimos la funcion.
    carpeta = os.getcwd() # creamos una variable que contenga la ruta en la que nos encontramos.
    nombre = input("Indroduce el nombre del fichero que quieres eliminar") # creamos una variable que contenga el nombre del archivo.
    if nombre not in carpeta: # si el archivo no existe en esta ruta.
        return print("El archivo que quiere eliminar no existe")
    else: # por el contrario si el archivo esta en la ruta en la que nos encontramos, eliminaremos el archivo.
        os.remove(nombre)
        return print("Se a eliminado el archivo",nombre)

def propNomFitxer(): # definimos la funcion.
    carpeta = os.getcwd() # creamos una variable que contenga la ruta en la que nos encontramos.
    nombre = input("Indroduce el nombre del fichero:") # creamos una variable que contenga el nombre del archivo.
    if nombre not in carpeta: # si el archivo no existe en esta ruta.
        return print("El archivo no existe.") # si el archivo no existe en esta ruta.
    else: # por el contrario si el archivo esta en la ruta en la que nos encontramos, nos dira el peso el archivo.
        peso = os.stat(nombre).st_size
        return print("El fichero,",nombre,"pesa",peso)

delNomFitxer() # Hacemos las llamadas al las funciones.
propNomFitxer()