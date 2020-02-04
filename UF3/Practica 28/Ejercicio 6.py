obrir = open("carregar_dades.txt", "rt") # Abrimos el archvio en formato read text.
diccionario = {} # creamos un diccionario vacio.
diccionario2 = {"Rojo":"Color","Hola":"Adios"}  #Creamos un diccionario con claves y valores.

# Esta funcion permite leer el formato clave y valor de un archivo, Itera el archivo para poder separar en elementos que son clave y valor
# una vez tenemos la clave y valor en un solo elemento, lo que hace es volver a separarla para conseguir dos elementos uno que sera la clave y el otro el valor
# Una vez que los tiene separados printa un diccionario que contiene las claves y los valores.
def carregar_dades(read):
    for linea in read:
        lista_valores = linea.split()
        for valor in range(len(lista_valores)):
            get_value = lista_valores[valor].split(':')
            diccionario[get_value[0]] = get_value[1]
        print(diccionario)
    obrir.close()

# Esta funcion pide un nombre al usuario para crear un archivo en modo escritura, una vez echo esto la funcion coge un diccionario que le hemos pasado previamente
# Cuando tiene este diccionario lo separa en clave y valor, una vez tenemos el diccionario separado, vamos a ir printando clave : valor y un espacio
def guardar_dades():
    archivo = input('Indroduce el nombre del archvio en el que quieres guardar el diccionario:')
    a = open(archivo+'.txt', "w")
    for linea in diccionario2:
        a.write(linea)
        a.write(':')
        a.write(diccionario2[linea])
        a.write(' ')
    a.close()

carregar_dades(obrir)
guardar_dades()
