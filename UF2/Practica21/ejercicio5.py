#creem les llistes i afegim les notes i noms a la seva respectiva llista.
lista_alumnes = []
lista_notes = []
quantitat = int(input('Introdueix el numero de notes i alumnes que vols introduir:'))
for i in range(quantitat):
    notas = int(input('Introdueix la nota:'))
    nombre = input('Introduiex el nom del alumne:')
    lista_alumnes.append(nombre)
    lista_notes.append(notas)

#definim la funció d'alumnes aprovats.
def aprovats(a,b):
    for i in range(len(b)):#Cada cop que el valor de i en la llista de notes sigui superior a 5.
        if b[i] >= 5:#imprimirem el nom del alumne que es en la posicio de la nota pero en la llista de alumnes.
            print(a[i])

#definim la funcio numero de alumnes aprovats.
def num_aprovats(b):
    comptador = 0 #posem un comptador.
    for i in b:#per cada cop que el valor de i en b sigui superior a 5 el comptador sumara 1.
        if i >= 5:
            comptador = comptador + 1
            print(comptador)#mostrem el nombre d'aprovats.

#definim la funcio de nota maxima.
def nota_maxima(a,b):
    for i in range(len(b)):#cada cop que el valor de i sigui 10, es mostrara el nom del alumne.
        if b[i] == 10:
            print(a[i])

#definim la funcio nota_mitja.
def nota_mitja(a,b):
    mitja = sum(b) / len(b)#creem la variable mitja en la cual calcularem la mitja de les notes.
    for i in range (len(b)):#Si el valor de i en la llista notes es igual o superior a la mitja.
        if b[i] >= mitja:#imprimirem el nom de la persona que esta en la posicio de la nota pero en la llista de alumnes.
            print(a[i])

#definim la funcio none
def none(a,b):
    nou_alumne = input('Introdueix el nom del alumne:')#demanarem el nom de un alumne.
    if nou_alumne in a:#si el nom es a la llista alumnes mostrarem la seva nota si no mostrarem none.
        nota = (b[a.index(nou_alumne)])
        print(nota)
    else:
        nota = 'None'
        print(nota)

#fem una crida a les funcions i substituïm les seves variables per la llista d'alumnes i la de notes.
print('Noms dels alumnes que han aprovat:')
aprovats(lista_alumnes,lista_notes)
print('Numero de alumnes que han aprovat:')
num_aprovats(lista_notes)
print('Noms dels alumnes que han arribat a la maxima puntuacio:')
nota_maxima(lista_alumnes,lista_notes)
print('Noms dels alumnes que han arribat a la nota mitja:')
nota_mitja(lista_alumnes,lista_notes)
print('Nota del estudiant si es a la llista')
none(lista_alumnes,lista_notes)