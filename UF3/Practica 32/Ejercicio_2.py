pacient= {"nom" : "Pep", "edat" : "42", "Diabetic" : "True"} # Creamos el diccionario.
archivo = open("exercicis/Data/operacions/pacients/pacients.txt", "w") # Abrimos el archivo en modo lectura.
for i in pacient: # Iteramos dentro del diccionario.
    valor = i + "\t" + pacient[i] + "\t"# Guardamos en una varaiable la clave mas su valor.
    archivo.write(valor) # Guardamos dicha informacion en un archivo.
archivo.close() # Cerramos el archivo.