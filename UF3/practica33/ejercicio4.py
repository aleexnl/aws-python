import os
def dir(a=os.getcwd()):
    for i in os.listdir(a):
        print("---",i)

def delete(fichero):
    os.remove(os.getcwd()+"/"+fichero)
    print("Se ha borrado el archivo "+fichero,"sin ningun problema.")
def prop(fichero):
    print("El archivo "+fichero,"pesa: ",os.stat(fichero).st_size)
while True:
    dir()
    opcion=input()
    if "del" in opcion:
        opcion=opcion.lstrip("del ")
        delete(opcion)
    elif "prop" in opcion:
        opcion=opcion.lstrip("prop ")
        prop(opcion)
    elif opcion=="exit":
        break
    else:
        print("Opcion no valida")