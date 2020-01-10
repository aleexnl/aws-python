from modules import functions as fc

while True:
    try:
        dividend = int(input("Introduce un dividendo: "))
        break
    except ValueError:
        print("ERROR: Introduce solo valores enteros")

while True:
    try:
        divisor = int(input("Introduce un divisor: "))
        break
    except ValueError:
        print("ERROR: Introduce solo valores enteros")

print(fc.recursive_div(dividend, divisor))
