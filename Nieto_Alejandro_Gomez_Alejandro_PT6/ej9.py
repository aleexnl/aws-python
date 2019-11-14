# Definimos la variable num donde saldra la cantidad de numeros que vamos a pedir
num=int(input("Cuantos numeros vas a introducir?: "))
# Ponemos las variables contador y negatius a 0
contador=0
negatius=0
# Entramos en el bucle siempre que contador sea mas pequeño que la cantidad de numero que vamos a pedir
while contador<num:
    # Sumamos a contador uno cada vuelta
    contador=contador+1
    # Pedimos un numero en cada vuelta
    num2=int(input("Dame el numero "+str(contador)+": "))
    # Decimos que si hay algun numero mas pequeño que 0 es decir un negativo, pues que a negativo se le sume uno en cada vuelta siempre y cuando el numero que hayamos puesto sea negativo
    if num2<0:
        negatius=negatius+1
# Finalmente mostramos la cantidad de numeros negativos que hay acompañado de un texto.
print("Has escrito "+str(negatius)+" numeros negativos")