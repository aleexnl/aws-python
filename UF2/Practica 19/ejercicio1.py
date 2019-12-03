'''Escriure el codi de la funció que retorna el quadrat d’un número que rep com
argument. Comprovar que funciona utilitzant un programa'''

#definimos una funcion para calcular el cuadrado de un numero y devolvemos el cuadrado.
def cuadrado_num(num):
    cuadrado = num **2 #elevamos el numero al cuadrado
    return cuadrado
#pedimos al usuario un numero.
num2 = int(input('numero'))
#hacemos un print a la funcion y sustituimos el numero que hemos pedido al usuario en la funcion.
print(cuadrado_num(num2))