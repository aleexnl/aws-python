def bin(x):
    if len(x) == 1:
        return x[0]
    else:
        return x[0] * bin(x[1:])
