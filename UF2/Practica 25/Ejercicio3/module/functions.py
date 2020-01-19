def sumapositivos(n):
    if n == 2:
        return n
    else:
        if n % 2 != 0:
            return sumapositivos(n - 1)
        else:
            return n + sumapositivos(n - 2)