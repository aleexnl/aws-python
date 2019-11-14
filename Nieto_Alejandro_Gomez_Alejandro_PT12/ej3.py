#Defino las variables para las diferentes maneras de hacerlo
contador=65
lista=[]
lista2=[]
lista3=[]
contador2=65
#Estamos diciendo que cuando el asci del contador sea diferente a Z entramos en el bucle
while chr(contador)!="Z":
    #Vamos añadiendo a la lista la letra que salga y sumamos al contador 1
    lista.append(chr(contador))
    contador=contador+1
#Añadimos a la lista la letra Z que se quedara fuera
lista.append("Z")
print(lista)
# ESto es lo mismo que el anterior que la diferencia que pondremos la condicion en un IF y no en el While
while True:
    lista2.append(chr(contador2))
    if chr(contador2)=="Z":
        break
    contador2 = contador2 + 1
print(lista2)

# Y en esta opcion si sabemos cual es el codigo ascci de la A y de Z, haremos un FOR y pondremos un rango desde el numero de A a la Z.
for i in range(65,91):
    lista3.append(chr(i))
print(lista3)