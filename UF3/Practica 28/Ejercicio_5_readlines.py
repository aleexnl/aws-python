file = open("origen.txt", "rt") # Abrimos el archivo origen en modo lectura de texto.
file2 = open("destinacion.txt", "w") # Abrimos el archivo destino en modo escritura.

linea = file.readlines() # Creamos una variable que contenga la lectura del fichero origen.
if linea != []: # Si la lista no esta vacia.
    for palabra in linea: # Para cada linea.
        for i in letra: # Para  cada letra.
            valor = (ord(i) + 13) % 26 # Creamos una variable que utilizaremos para codificar el texto.
            file2.write(chr(valor)) # Escribimos en el archivo destino, el texto codificado.
file.close() # Cerramos los ficheros.
file2.close()

