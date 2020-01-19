def suma(n):  # Definimos la funcion
    if n >= 1:  # Definimos una condicion
        suma(n-1)  # Llamamos a la funcion
        print(n)  # Mostramos el valor de el parametro
