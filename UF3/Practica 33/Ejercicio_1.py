import os
import shutil
# Este try lo que hace es intentar crear la carpeta Temp y mostrar el directorio de la carpeta.
# En el caso de que exista el except se encarga de eliminarla (sin importar si hay archivos o no)
try:
    os.mkdir('Temp')  # Crear directorio
    os.chdir('Temp')  # Moverse a directorio
    print("S'ha creat la carpeta", os.getcwd())  # Mostrar directorio actual
except FileExistsError:
    os.chdir('Temp')
    print("S'ha eliminat la carpeta", os.getcwd())
    os.chdir('../')
    shutil.rmtree('Temp')  # Borrar arbol de directorio
