archivo = open("ejercicio4.txt", "r")
lineas = 0
palabra = 0
caracters = 0
for i in archivo.readlines():
    lineas += 1
    caracters += len(i)
    texto =i.split()
    palabra += len(texto)
print("Tiene", lineas ,"lineas")
print("Tiene",palabra, "Palabras")
print("Tiene",caracters, "Caracteres")
archivo.close()

