file = open("origen.txt", "rt") # Abrimos el archivo origen en modo lectura de texto.
file2 = open("destinacion2.txt", "w")  # Abrimos el archivo destino en modo escritura.

linea = file.read() # En linea almacenamos el contenido del archvio origen, en formato string.
if linea != '': # Si la string no esta vacia
    for letra in linea: # Para cada letra en la string
        valor = (ord(letra) + 13) % 26 # Creamos una variable que utilizaremos para codificar el texto.
        file2.write(chr(valor)) # Escribimos en el archivo destino, el texto codificado.
file.close() # Cerramos los ficheros.
file2.close()