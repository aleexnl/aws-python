import math # Aqui importamos la libreria de math
coordenadas = {}# Hacemos un diccionario que este vacio
''' Haremos un bucle que pida las corrdenadas de x y de y y que se guarden en el diccionario vacio, en la primera vuelta se guardaran 
las primeras coordenadas y en las segundas las segundas cordenadas. '''
for i in range(2):
    print("Coordenadas del punto", i+1)
    x = int(input("Coordenada de x: "))
    y = int(input("Coordenada de  y: "))
    coordenadas[i+1] = x, y # Aqui guardaremos las dos coordenadas en el diccionario
print(coordenadas)# Printamos las coordenadas
''' Guardamos las diferentes cooordendas cada una con su valor'''
x1 = coordenadas[1][0]
y1 = coordenadas[1][1]
x2 = coordenadas[2][0]
y2 = coordenadas[2][1]
''' Y finalmente printaremos el resultado de la operacion'''
print (math.sqrt(((x2 - x1)**2) + (y2-y1)**2))

