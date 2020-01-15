def recursive_div(divend, divsor): # creeamos la funcion y le añadimos dos valores.
    if divend == 0: # si el dividendo es = 0 nos devolvera 0.
        return 0
    elif divend < divsor: # cuando el dividendo sea mas pequeño que el divisor nos devolvera como valor 1.
        return 1
    else: # En caso de que las otras condiciones no se hayan cumplido entraremos en esta.
        return 1 + recursive_div(divend - divsor, divsor)
