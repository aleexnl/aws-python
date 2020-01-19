def vector_check(vector_one, vector_two):  # Llamada a la funcion
    if vector_one[0] == vector_two[0]:  # Si la posición del vector 1 es igual que la del dos devuelve true
        return True
    else:
        if vector_one[-1] == vector_two[-1]:  # Si la posición del vector 1 es igual que la del dos
            return vector_check(vector_one[:-1], vector_two[:-1])  # Llamamo ¡s a la función restandole uno a la lista
        else:
            return False  # Si no se cumple la condición directamente devolvemos false
