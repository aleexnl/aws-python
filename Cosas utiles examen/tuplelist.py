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

''' EJEMPLO FOR ANIDADO EXAMEN'''


# Recoje el valor entero que introduce el usuario y lo almacena en la variable "largo"
largo = int(input("largo = "))
# Recoje el valor entero que introduce el usuario y lo almacena en la variable "alto"
alto = int(input("alto = "))

# Por i en el rango de 0 a el valor de alto
for i in range(alto):
    # Por i en el rango de 0 a el valor de largo
    for j in range(largo):
        '''

        Condiciones para que solo se cumple la escritura del caracter *

        Cuando cumpla las siguientes condiciones
        - i es igual a 0 o el valor de alto-1 y j es igual a 0 o el valor de largo-1
        - i es igual a 1 o el valor de alto-2 y j es diferente a 0 y a largo-1
        - i es igual a 2 o el valor de alto-3 y j es igual a 1 o el valor de largo-2

        '''
        if (i == 0 or i == alto - 1) and (j == 0 or j == largo - 1) or (i == 1 or i == alto - 2) and (
                j != 0 and j != largo - 1) or (i == 2 or i == alto - 3) and (j == 1 or j == largo - 2):
            # Muestra en pantalla el caracter * y evita el salto de linea por defecto de print
            print("*", end="")
        else:
            # Muestra en pantalla un espacio " " y evita el salto de linea por defecto de print
            print(" ", end="")
    # Muestra el salto de linea del final del print
    print("")


''' EJERCICIO BINARIO EXAMEN '''

# Inicializa la variable num a 0
num = 0
# Mientras el valor de num sea menor a 1 o mayor a 255
while num <1 or num > 255:
    # Recoje el numero entero introducido por el usuario y lo almacena el la variable num
    num = int(input("Introdueix un num per calcular el seu valor binari: "))

    # Si el valor de num es menor o mayor a 255
    if num < 1 or num > 255 :
        # Muestra en pantalla que el numero no es valido
        print("El num no es valid (nomes el nums del 1 al 255)")
# Inicializa la variable binari como una string vacia
binari=""
# Mientras el valor de num sea mayor a 0
while num>0:
    # Establece el resultado de num modulo de dos como string en la variable "r"
   r = str(num%2)
    # Establece el valor de num con el resultado de num division entera de 2
   num = num//2

    # Concatena el contenido de la variable r al principio de la string binari
   binari=r+binari
# Muestra en pantalla el contenido de la variable binari
print(binari)
