def desglossament():  # Definimos la la funcion.
    total = {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}  # Definimos un diccionario con todos los
    # valores disponibles.
    """ Este bucle lo que hace es comprobar que el valor introducido sea de tipo integro y que sea mayor que 0 """
    while True:  # Iniciamos bucle.
        try:  # Intentar esta opcion
            qty = int(input("Introduce la cantidad de euros exacta: "))  # Pedir cantidad
            if qty > 0:  # Si es mayor que 0, acabar bucle
                break  # Acabar bucle
            if qty <= 0:  # Si es menor o igual a 0:
                print("¡Introduce un valor mayor que 0!")  # Mostramos error
        except ValueError:  # Definimos la excepcion de si el valor no es del tipo correcto
            print("¡Introduce solo valores enteros!")  # Mostramos error
    temp = qty  # Asignamos el valor de qty a temp, para trabajar con ella y no perder el valor
    """Este bucle lo que hace es iterar con cada valor del diccionario, para conseguir el cuociente y el residuo y, 
    luego asignarlo a la clave misma para obtener el total de billetes usados """
    for i in total:  # Iniciamos el bucle
        total[i] = temp // i  # Calcular cuociente
        temp = temp % i  # Calcular residuo
        if temp == 0:  # Si el residuo es 0, acabar el bucle
            break  # Acabar el bucle
    print(total)  # Mostramos la lista


desglossament()  # Llamamos a la funcion
