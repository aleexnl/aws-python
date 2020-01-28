''' Este try lo qu ehace es abrir el comprobar que el archivo existe. Si existe simplemente se cerrará y listo.
 En el caso de que no existiera el archivo se crearia de 0 y se le añadirian lineas para evitar que este vacio.
 Al final del try se cierra el archivo para perder la posición del puntero.'''

try:
    print('[INFO] Abriendo Ejercicio1.txt')
    file = open('Ejercicio1.txt')
except FileNotFoundError:
    print('[ERROR] Archivo no encontrado. Creando archivo...')
    file = open('Ejercicio1.txt', 'w')
    file.write('¡Hello World!\nThis is a sample text\nso we can test\nthe code that you are executing\n¡Im sure this is working!')
finally:
    file.close()

file = open('Ejercicio1.txt')  # Abre el archivo en modo lectura. No esta especificado porque el modo r es default

# Este bucle while True se asegura de que nuestro input se cumpla de una manera correcta; pide un valor numerico
# y si este no es correcto simplemente cubre el error con el except y lo seguirá pidiendo hasta que sea correcto.
# Una vez haya un valor en el input, el finally ejecutará el break para salir del bucle y continuar con el codigo.
while True:
    try:
        hm_lines_to_print = int(input('[INFO] Introduce hasta que linea quieres mostrar: '))
    except ValueError:
        print('[ERROR] Introduce solo datos numericos enteros.')
    finally:
        break

print('\n')  # Añade un espacio en blanco

# Este bucle lo que hace es ejecutar el codigo en su interior tantas veces como se especifico en el input anterior.
# El codigo del interior simplemente muestra las lineas siguiendo el 'indice' del cursor.
# (el end='' sirve para eviar que se muestren espaciados innecesarios)
for line in range(hm_lines_to_print):
    print(file.readline(), end='')


