def meths(num, den):
    if den == 1:
        return 4
    if num < den:
        return num / den * meths(num, den - 2)
    else:
        return num / den * meths(num - 2, den)
