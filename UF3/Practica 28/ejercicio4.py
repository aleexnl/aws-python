# abrivos el archivo de modo lectura con "r"
archivo = open("ejercicio4.txt", "r")
# Creamos varables lineas, palabras, caracters con el valor inicialmente 0
lineas = 0
palabra = 0
caracters = 0
# creamos un bucle que nos pasara por todas las lineas del archivo
for i in archivo.readlines():
    lineas += 1
    caracters += len(i)
    texto =i.split()
    palabra += len(texto)
# Finalmente printamos las variables para que nos printe todas lineas, palabras
# y caracters que tiene el arhivo,
print("Tiene", lineas ,"lineas")
print("Tiene",palabra, "Palabras")
print("Tiene",caracters, "Caracteres")
archivo.close()