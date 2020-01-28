# Escriure un programa que copiï tot el contingut d'un arxiu (sigui de text o binari) a un altre, de manera que quedi
# exactament igual.  Nota: Utilitzar la funció read(Numbytes) per llegir com a màxim una quantitat de bytes.


''' Este try lo que hace es abrir y comprobar que el archivo existe. Si existe simplemente se cerrará y listo.
 En el caso de que no existiera el archivo se crearia de 0 y se le añadirian lineas para evitar que este vacio.
 Al final del try se cierra el archivo para perder la posición del puntero.'''

try:
    print('[INFO] Abriendo Ejercicio2.txt')
    file = open('Ejercicio2.txt')
except FileNotFoundError:
    print('[ERROR] Archivo no encontrado. Creando archivo...')
    file = open('Ejercicio2.txt', 'w')
    file.write('¡Hello World!\nThis is a sample text\nso we can test\nthe code that you are executing\n¡Im sure this is working!')
finally:
    file.close()

# Este try lo que hace es abrir y comprobar que el archivo existe. Si existe simplemente se cerrará y listo.
# En el caso de que no existiera el archivo se crearia de 0 y se le añadirian lineas para evitar que este vacio.
# Al final del try se cierra el archivo para perder la posición del puntero.

try:
    print('[INFO] Abriendo Ejercicio2_copy.txt')
    file = open('Ejercicio2_copy.txt')
except FileNotFoundError:
    print('[ERROR] Archivo no encontrado. Creando archivo...')
    file = open('Ejercicio2_copy.txt', 'w')
finally:
    file.close()

original_file = open('Ejercicio2.txt')  # Abrir archivo en modo lectura.
copy_file = open('Ejercicio2_copy.txt', 'w')  # Abrir archivo en modo append (igual que write, pero no sobrescribe)

copy_file.write(original_file.read())  # Copiamos el contenido del archivo origen al archivo destino.