qty = int(input("Introduce la cantidad de datos a introducir: "))
data = []
for i in range(qty):
    tmpdata = []
    name = str(input("Introduce tu nombre: "))
    sname = str(input("Introduce tu apellido: "))
    iname = str(input("Introduce tu inicial del segundo nombre: "))
    tmpdata.append(sname), tmpdata.append(name), tmpdata.append(iname)
    data.append(tmpdata)
for j in range(len(data)):
    print(data[j][1], data[j][2], ".", data[j][0])
