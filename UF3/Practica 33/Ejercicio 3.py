import os # Importamos os que nos permitara acceder a funcionalidades dependientes del sistema operativo.

file = input("Quin es el nom del fitxer a cercar?") # Creamos una variable llamada file para pedir al usuario que nos introduzca nombre del usuario.
ruta = input("Escriu el nom d'una ruta a una carpeta:")# Creamos otra variable para pedir al usuario que nos introduzca la ruta relativa

def CercarFixter(x,y):
    if x in os.listdir(y):# Con esta condicion estamos deciendo que nos mire el contenidos
        print("S'ha trobat el fitxer a :" +y+'/'+x)# Con este print printamos en la pantalla el resultado de la ruta obtenida del fichero
    for i in os.listdir(y):
        if os.path.isdir(i) == True:# Usamos un if para contener la ruta del fichero.
             buscar(x,y+'/'+i)

CercarFixter(file,ruta) # Hacemos la llamada a la funcion