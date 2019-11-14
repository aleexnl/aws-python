lst = []
psc = int(input("Introduce posicion: "))
qty = int(input("Introduce cantidad de nombres a introducir: "))
for i in range(qty):
    lst.append(input("Introduce un nombre: "))
i = psc
for i in range(len(lst)):
    print("Querido", lst[i], "me alegro de verte")
