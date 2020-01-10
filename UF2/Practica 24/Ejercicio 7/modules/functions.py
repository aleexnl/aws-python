def producto_recursivo(x, y):
    if y == 1:
        return x
    else:
        return x + producto_recursivo(x, y-1)
