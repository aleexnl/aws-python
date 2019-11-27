lst = [1, 2, 3, 4, 5, 6] # Creamos la lista y le insertamos unos valores
k = 3 # Creamos la variable con el numero K
'''Aqui crearemos las 3 listas donde iremos guardando los numeros segun las comparaciones que nos pidan '''
max = []
min = []
mul = []
igual = []
''' Aqui lo que estamos haciendo es que por cada numero que hay en la lista se hagan las diferentes comparaciones (para saber los
mayores, menores y multiples de K) '''
for i in lst:
    if i > k:
        max.append(i)
    elif i < k:
        min.append(i)
    else:
        igual.append(i)
    if k%i == 0:
        mul.append(i)
''' Printamos todas las listas acompañadas de un texto '''
print("La lista es: "+str(lst))
print("El numero es: "+str(k))
print("La lista de numeros mayores es: "+str(max))
print("La lista de numeros menores es: "+str(min))
print("La lista de numeros iguales es: "+str(igual))
print("La lista de numeros multiples es: "+str(mul))
