def fibonacci(a):
    if a == 0 or a == 1:
        return a
    else:
        return fibonacci(a - 1) + fibonacci(a - 2)



