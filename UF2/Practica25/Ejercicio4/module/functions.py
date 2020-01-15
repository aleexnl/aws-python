def MCD(a, b):
    if a % b == 0:
        return b
    else:
        return MCD(b, a % b)