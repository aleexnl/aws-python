def randomarray(n):  # Definimos la fucnion
    if len(n) == 1 and n[0] % 3 != 0:  # definimos caso base para detener ercursividad
        return 0  # Devolvemos valor
    if len(n) == 1 and n[0] % 3 == 0:  # definimos otro caso base para detener ercursividad
        return n[0]  # Devolvemos valor
    else:  # Cualquier otro caso
        if n[len(n)-1] % 3 == 0:  # Definimos una condición para acceder a la recursividad
            return n[-1] + randomarray(n[:-1])  # Llamamos a la funcion recurisvamente
        else:  # Cualquier otro caso
            return randomarray(n[:-1])  # Llamamos a la funcion recurisvamente
