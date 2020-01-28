archivo = open("ejercicio4.txt", "r")
lineas = 1
palabra = 1
caracters = 0
for i in archivo.readlines():
    lista = i
    lineas += i.lineas
    caracters += caracters
    texto = i.split()
    palabra += len(texto)
print(lineas)
print(palabra)
print(caracters)
archivo.close()

