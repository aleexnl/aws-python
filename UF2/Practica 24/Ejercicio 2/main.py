from modules import functions as fc

while True:
    try:
        num = int(input("Introduce un numero: "))
        break
    except ValueError:
        print("ERROR: Introduce solo valores enteros")

print(fc.sum_digit_in_number(num))
