''' Creamos las listas de septiembre y de diciembre y despues una donde se guardara la diferendia de alturas'''
sept = []
dic = []
dif = []
print("Alçada de septiembre: ") # Ponemos esto para indicar al usuario que las alturas que va a poner ahora son de septiembre
''' A qui basicamente estamos diciendo que pida 10 veces una altura y vaya guardando todas en la lista de septiembre '''
for i in range(2):
    sept.append(float(input("Alçada "+str(i)+": ")))

''' A qui hacemos exactamente lo mismo que en el FOR anterior pero añadiendolo en la lista de diciembre '''
for i in range(2):
    dic.append(float(input("Alçada "+str(i)+": ")))
''' Aqui diremos que vaya haciendo la resta entre la posicion I de la lista de Diciembre con la de Septiembre y vaya guardando 
 la diferencia en la lista de diferencias.'''
for i in range(len(sept)):
    op = ('{0:.2}'.format(dic[i] -sept[i])) # Aqui lo que estamos haciendo es que reducimos los decimales a 2
    dif.append(op)
''' Finalmente printaremos todas las listas'''
print("La lista de sepriembre és: "+ str(sept))
print("La lista de diciembre és: "+ str(dic))
print("La lista de diferencias és: "+ str(dif))
