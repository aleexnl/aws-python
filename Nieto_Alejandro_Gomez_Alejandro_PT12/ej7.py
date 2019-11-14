# Creamos una lista con diferentes palabras
lista=["hola","ADIOS","mañana","Futbol"]
# Decimos que I vaya dando vueltas hasta la lonigitud de la lista
for i in range(len(lista)):
    # Y diremos que en la posicion de la lista que sea el numero de la vuelta (I) que en esa cadena se combiertan todas las letras a minuscula
    lista[i]=lista[i].lower()
# Ordenaremos la lista y la printaremos
lista.sort()
print(lista[0])
