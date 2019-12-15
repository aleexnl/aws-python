from matematiques import operacions_basiques as ob


while True:
    try:
        number1 = float(input("Introduce el primer numero: "))
        number2 = float(input("Introduce el segundo numero: "))
        break
    except ValueError:
        print("ERROR: Introduce solo numeros.")


print(ob.sum_numbers(number1, number2))
print(ob.sub_numbers(number1, number2))
print(ob.multi_numbers(number1, number2))
print(ob.div_numbers(number1, number2))
