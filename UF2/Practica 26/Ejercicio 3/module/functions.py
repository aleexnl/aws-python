def multiplicacio(x, y):  # definimos la funcion
    if y == 0:  # ponemos los casos base
        return 0
    if y == 1:  # cuando y es 0 devolvemos 0 y cuando es 1 devolvemos y, cuando x es 1 devolvemos y
        return x
    if x == 1:
        return y
    if y % 2 == 0:  # si b es par aplicamos esta formula
        return multiplicacio((2 * x), (y // 2))
    if y % 2 != 0:  # si b es impar aplicamos esta otra formula
        return x + multiplicacio((2 * x), (y//2))
