''' Creamos 2 listas de variables vacias y otra donde guardaremos los literales '''
llistasAlumne = []
llistasNotes = []
literals = ["suspés", "suspés", "suspés", "suspés", "suspés", "suficient", "bé", "notable", "notable", "excelente", "excelente"]

''' Aqui definiremos los dos bucles  '''
for i in range (2): # En este diremos que en un rango de 8 pida el nombre y la nota del alumno .
    llistasAlumne.append(input("Dame el nombre del alumno "+ str(i+1) + ": "))
    llistasNotes.append(int(input("Dame la nota del alumno (tiene que ser un entero) "+ str(i+1) + ": ")))
for b in range(len(llistasAlumne)): # En este bucle printaremos los resultados .
    print(llistasAlumne[b]+ " ha obtingut un "+ literals[llistasNotes[b]])
