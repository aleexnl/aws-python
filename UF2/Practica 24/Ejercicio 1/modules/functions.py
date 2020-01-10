def recursive_div(divend, divsor):
    if divend == 0:
        return 0
    elif divend < divsor:
        return 1
    else:
        return 1 + recursive_div(divend - divsor, divsor)
