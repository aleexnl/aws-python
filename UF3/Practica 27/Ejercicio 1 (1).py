f = open("parells.txt", "w+") # Abrimos los ficheros fichero
g = open("senars.txt", "w+")

for i in range(1,100+1): # Para i en un rango de 1 a 100
    if i % 2 == 0: # Si i es par, escribimos i en el fichero parells
        f.write(str(i))
        f.write("\n")
    else: # Si no es par, escribimos i en el fichero parells
        g.write(str(i))
        g.write("\n")

f.close() # Cerramos los ficheros
g.close()