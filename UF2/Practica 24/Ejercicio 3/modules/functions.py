# Dado una lista de n numeros, sumar estos recursivamente


def recursive_sum(num_list, i): # Creamos la funcion y le ponemos dos valores.
    if i == len(num_list) - 1: # Si el valor de i es igual a la longitud de la lista - 1
        return num_list[i] # Nos devolvera el numero que ocupa la posicion i en la lista.
    return num_list[i] + recursive_sum(num_list, i + 1) # Si no cumple la otra condicion entra y realiza este calculo.
