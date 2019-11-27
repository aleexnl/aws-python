alum = {}
for i in range(3):
    dni = int(input("Introduce el DNI del alumno"))
    temp = int(input("¿Cuantas materias cursa?"))
    while temp < 1:
        print("¡Tiene que cursar en alguna materia!")
        temp = int(input("¿Cuantas materias cursa?"))
    for j in range(temp):
        materias = []
        materia = str(input("Introduce la materia: ")).lower()
        materias.append(materia)
    while len(materias) < 1:
        print("¡Tienes que meter una materia!")
        materia = str(input("Introduce la materia: ")).lower()
        materias.append(materia)
    for k in range(len(materias)):
        temp = bool(input("Introduce la nota del alumno: "))
        alum[dni] = [tuple(materias[k][temp])]
print(alum)
