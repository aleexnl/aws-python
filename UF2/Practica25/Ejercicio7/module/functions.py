def randomarray(n):
    if len(n) == 1 and n[0] % 3 != 0:
        return 0
    if len(n) == 1 and n[0] % 3 == 0:
        return n[0]
    else:
        if n[len(n) -1] % 3 == 0:
            return n[-1] + randomarray(n[:-1])
        else:
            return randomarray(n[:-1])
