from modules import functions as fc

number_list = []
print("INTRODUCE UN NUMERO NEGATIVO PARA ACABAR")
while True:
    try:
        number = int(input("Introduce un numero: "))
        if number >= 0:
            number_list.append(number)
        elif number < 0:
            break
    except ValueError:
        print("ERROR: Introduce solo valores enteros")

print(fc.recursive_sum(number_list, 0))
