# Dado una lista de n numeros, sumar estos recursivamente


def recursive_sum(num_list, i):
    if i == len(num_list) - 1:
        return num_list[i]
    return num_list[i] + recursive_sum(num_list, i + 1)
