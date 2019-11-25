''' EJERCICIO 2'''

''' Definimos las variables '''
frase =" On the border line and of the edge and where I walk alone " # En esta ponemos la frase
palabraslist = frase.split() # Aqui lo que hacemos es una lista con las palabras de la frase separadas
diccionario=dict.fromkeys(palabraslist) # Y aqui convertimos la lista creada anteriormente a claves en un diccionario

''' Hacemos un bucle en el cual diremos que vaya recorriendo las palabras de la lista y en la clave del diccionario 
que tenga ese nombre añadiremos las veces que aparece en la frase con un count a la lista creada con las palabras'''
for i in palabraslist:
   diccionario[i]=palabraslist.count(i)
print(diccionario) # Finalmente lo printamos


''' EJERCICIO 2.3'''

''' Iniciamos un diccionario y una lista '''
diccionario2={}
lista=[]
''' En este for lo que hacemos es una lista con todas las letras de la frase para transformarlo en claves despues'''
for i in frase.lower():
   if i != ' ':
      lista.append(i)

''' Aqui es cuando hacemos la conversion indicada anteriormente '''
diccionario2=dict.fromkeys(lista)

''' Y por ultimo hacemos lo mismo que en el ejercicio 2 para que se vayan añadiendo a cada clave su valor
(en este caso es el numero de veces que aparece esa letra en la frase )'''
for b in diccionario2:
   diccionario2[b]=lista.count(b)
print(diccionario2) # Y por ultimo lo printamos

