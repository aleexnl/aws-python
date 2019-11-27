num = str(input("Introduce un numero: "))
list = []
for i in num:
    list.append(i)
list.reverse()
num = []
for i in range(len(list)):
    num.append(i)
    if i+1 % 3 == 0:
        if i != 0:
            num.append(".")
print(num)