def sum_digit_in_number(number): # Creamos la funcion y le añadimos un valor
    if 10 > number > 0: # Si el numero introducido es mas pequeño que 10 y mas grande que 0
        return number # Devolvemos el numero intorducido
    return number % 10 + sum_digit_in_number(number // 10) # Si el numero no cumple la anterior condicion entra aqui.
