f = open("parells.txt", "rt") # Abrimos los ficheros fichero
g = open("senars.txt", "rt")
h = open("1a100.txt", "w+")

for i in range (1,100+1): # En un rango del 1 al 100, vamos intercalando una linea del fichero senars y otra del fichero parells
    h.writelines(g.readline())
    h.writelines(f.readline())

f.close() # Cerramos los ficheros
g.close()
h.close()
