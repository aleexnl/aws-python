llistaAlumne = []
llistaNotes = []
lit = ["suspés", "suspés", "suspés", "suspés", "suspés", "aprovat", "bé", "notable", "notable", "excelente", "excelente"]
for i in range (9):
    llistaAlumne.append(input("Inserta el nombre del alumno " + str(i+1) + ": "))
    llistaNotes.append(int(input("Inserta la nota del alumno (tienen que ser numeros enteros) " + str(i+1) + ": ")))
for b in range(9):
    print(llistaAlumne[b] + " ha obtingut un " + lit[llistaNotes[b]])
