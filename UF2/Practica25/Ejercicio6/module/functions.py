# f(x) = x*2 +
# (x − 1)*2 +
# (x − 2)*2 +
# 2*2 +
# 1*2


def calc(num):  # Definimos la funcion.
    if num == 1:  # Definimos el caso base para detener la recursividad.
        return 2  # Devolvemos el valor 2
    else:  # Cualquier otra cosa.
        return 2 * num + calc(num - 1)  # Llamamos a la funcion recrusivamente.

