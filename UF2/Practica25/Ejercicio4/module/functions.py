def mcd(a, b):  # Definimos la funcion con sus parametros
    if a % b == 0:  # Ponemos el caso base
        return b   # Devolvemos el valor b para detener la función
    else:  # Una condicion que mientras que no se cumpla el caso base llamamos a la funcion recursivamente
        return mcd(b, a % b)
