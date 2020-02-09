# Importamos os que nos permitara acceder a funcionalidades dependientes del sistema operativo.
import os
# Creamos una variable llamada file para pedir al usuario que nos introduzca nombre del usuario.
file = input("Introduce el nombre del archivo que quieres introducir")
# Creamos otra variable para pedir al usuario que nos introduzca la ruta relativa
ruta = input("Indroduce la ruta relativa donde quieres buscar")
# Definemos una variable llamada buscar y passamos dos parametros, que hemos puesto x e y.
def buscar(x,y):
# Con esta condicion estamos deciendo que nos mire el contenidos
    if x in os.listdir(y):
# Con este print printamos en la pantalla el resultado de la ruta obtenida del fichero
        print("ha trobat el fitxer a :" +y+'/'+x)
    for i in os.listdir(y):
# Usamos un if para contener la ruta del fichero.
        if os.path.isdir(i) == True:
             buscar(x,y+'/'+i)
# Finalmente printamos en la pantalla la funcion definida.
buscar(file,ruta)