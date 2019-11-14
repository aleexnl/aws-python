while True:
    rango=int(input("Cuantos numeros vas a introducir?: "))
    if rango>0:
        break
    else:
        print("¡ IMPOSIBLE !")

num1=int(input("Escribe un numero: "))

i=0
rango=rango-1
while i<rango:
    i = i + 1
    num2=int(input("Escribe un numero diferente a "+str(num1)+": "))
    if num1!=num2:

        num1=num2

    else:
        print("¡" + str(num1) + " es igual que " + str(num2))

print("Gràcias por tu colaboracion")