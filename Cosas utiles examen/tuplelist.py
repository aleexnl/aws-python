''' PRUEBA DE LISTA DE TUPLAS CON INPUTS'''
lista = []
for i in range(2):
    a=input("Dame argo")
    b=input("Dame otra cosa")
    tupla=(a, b)
    lista.append(tupla)

print(lista[1])

''' PRUEBA DEL END'''
lista2 = ['Hola', 'Adios', 'Pene', 'Coño']

for i in lista2:
    print(i, end=' ')

''' EJEMPLO FOR ANIDADO '''

a = int(input("Amplada: "))
h = int(input("Alçada: "))

for tmph in range(h):
    for tmpa in range(a):
        if tmph == h-1 or tmph == 0:
            print("*", end="")

        else :
            if tmpa == a-1 or tmpa == 0:
                print("*", end="")
            else :
                   print(" ", end="")
    print("")