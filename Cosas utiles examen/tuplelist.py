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
