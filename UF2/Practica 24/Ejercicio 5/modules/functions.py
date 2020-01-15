def rus(a, b): # Creamos la funcion.
    if a == 1: # Si a es 1 devolvemos el valor de b.
        return b
    if a % 2 != 0: # Si a modulo 2 es diferente a 0.
        return b + rus(a // 2, b * 2) # Realizamos esta operacion.
    else: # En caso contrario realizamos estas otra.
        return rus(a // 2, b * 2)
