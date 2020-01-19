def elevado(a,b): # definimos la funcion
    if b == 0: # ponemos los casos base
        return 1 # cuando b es 0 devolvemos 1 y cuando es 1 devolvemos a
    if b == 1:
        return a
    if b % 2 == 0: # si b es par aplicamos esta formula
        return  elevado(a, b // 2) ** 2
    if b % 2 != 0: # si b es impar aplicamos esta otra formula
        return a * elevado(a, b // 2) ** 2
