def sum_numbers(num1, num2):
    return "Suma: ", num1 + num2


def sub_numbers(num1, num2):
    return "Resta: ", num1 - num2


def multi_numbers(num1, num2):
    return "Multiplicacion: ", num1 * num2


def div_numbers(num1, num2):
    try:
        return "Division: ", num1 / num2
    except ZeroDivisionError:
        return "ERROR: No es pot dividir entre 0"
