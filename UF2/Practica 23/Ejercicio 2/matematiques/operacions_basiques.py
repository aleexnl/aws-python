def sum_numbers(num1, num2):
    return num1 + num2


def sub_numbers(num1, num2):
    return num1 - num2


def multi_numbers(num1, num2):
    return num1 * num2


def div_numbers(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "ERROR: No es pot dividir entre 0"
