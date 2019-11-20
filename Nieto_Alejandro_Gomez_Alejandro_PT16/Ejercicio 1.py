dicc = {}
phrase = str(input("Introduce una frase"))
wrds = phrase.split()
for i in range(0, len(wrds)):
    print("Posicion", wrds[i])
    for j in range(len(wrds[i])):
        print("Palabra", j)
