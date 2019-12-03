#definimos una funcion para calcular el cuadrado de un numero y devolvemos el cuadrado.
def cuadrado_num(num):
    cuadrado = num **2
    return cuadrado
#pedimos al usuario un numero.
num2 = int(input('numero'))
#hacemos un print a la funcion y sustituimos el numero que hemos pedido al usuario en la funcion.
print(cuadrado_num(num2))