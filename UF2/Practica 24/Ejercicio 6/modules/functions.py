def potencial(x, y):
    if y == 1:
        return x
    return x * potencial(x, y-1)
