import os
import shutil


def show_input():
    print('CAMBIO DE EXTENSIONES')
    print('Introduce la EXTENSION ORIGEN y la EXTENSION DESTINO')
    print('separado por espacio')
    extensions = input()
    prepare_extensions(extensions)


def prepare_extensions(arg):
    extensions = arg.split()
    if len(extensions) > 2:
        print('¡HAS INTRODUCIDO MAS DE DOS VALORES!')
        show_input()
    elif len(extensions) < 2:
        print('¡HAS INTRODUCIDO MENOS DE DOS VALORES!')
        show_input()
    check_extensions(extensions)


def check_extensions(args):
    if len(args[0]) != 3:
        print('ERROR: La extension', args[0], 'no es correcta.')
        show_input()
    elif len(args[1]) != 3:
        print('ERROR: La extension', args[1], 'no es correcta.')
        show_input()


show_input()
