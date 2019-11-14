# Entramos en el bucle si o si
while True:
    # Pedimos la base y el exponente
    b = int(input("Dame la base: "))
    e = int(input("Dame el exponente: "))
    # Decimos que si la base y el exponente son mas grandes que 0 es decir no son negativos, salgamos del break y hagamos la operacion con los dos numeroes que hemos pedido
    if b>0 and e>0:
        break
    # Si nos insertan algun numero negativo tanto ene el exponente como en la base pues repetiremos el bucle.
print(b**e)