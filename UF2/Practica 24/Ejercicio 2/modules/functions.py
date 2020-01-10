def sum_digit_in_number(number):
    if 10 > number > 0:
        return number
    return number % 10 + sum_digit_in_number(number // 10)
