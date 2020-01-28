lista = ["nombre", "fecha", "horas", "signatura"]
archivo = open("ejercicio.txt","r")
delimitador = " : "
contador = len(archivo.readline())
archivo.seek(0)
for i in range(1, contador-1):
    print(lista[i-1], delimitador, archivo.readline())
archivo.close()


