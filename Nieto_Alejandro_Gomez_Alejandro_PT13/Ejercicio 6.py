chains = ["Buenos dias ", "Buenas tardes ", "Buenas noches ", "Saludos, "]
namelst = []
name = str(input("Introduce tu nombre: "))
fname = str(input("Introduce tu apellido: "))
sname = str(input("Introduce la inicial de tu segundo nombre: "))
namelst.append(name), namelst.append(fname), namelst.append(sname)
print(namelst)
print(namelst[0], namelst[2], ".", namelst[1])