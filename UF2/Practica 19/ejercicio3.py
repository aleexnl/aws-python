'''Escriure el codi de la funció que imprimeixi per pantalla tots els divisors del
número que rep com argument.'''

#definimos una funcion para calcular todos los divisores de un numero y los imprimimos.
def divisores(num):
    for i in range(1,num+1):#desde 1 hasta el numero introducido
        if num % i == 0:#vamso probando a ver si al dividirlo el residuo da 0
            print(i)
#pedimos al usuario un numero.
num2 = int(input('Introduce un numero para saber sus divisores:'))
#sustituimos el numero que ha dado el usuario en la funcion y nos imprimira los divisores.
divisores(num2)