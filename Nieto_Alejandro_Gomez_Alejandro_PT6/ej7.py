# Definimos una variable contador a 0
contador=0
# Pedimos la altura y la anchura
a=int(input("Introduce el ancho del rectangulo: "))
h=int(input("Introduce la altura del rectangulo: "))
#Printamos tantos asteriscos como anchura hay
print("*"*a)
# Y entramos en el bucle diciendo que si contador es mas pequeño que altura-2
while contador<h-2:
    #Entonces sumamos al contador 1 en cada vuelta
    contador=contador+1
    # Y printaremos tantos asteriscos con separaciones entre ellos que varian segun la anchura menos los dos asteriscos que mostraremos para que quede
    print("*"+" "*(a-2)+"*")
print("*"*a)
