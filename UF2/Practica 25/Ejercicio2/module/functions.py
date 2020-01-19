def invertir(n):
    if len(n) == 1:
        return n
    else:
        return n[-1] + invertir(n[0:len(n)-1])

def invertir(n, y):
    if n < 10 and y > 0:
        return n
    else:
        return (n % 10) * (10 ** (y-1)) + invertir(n // 10, y - 1)