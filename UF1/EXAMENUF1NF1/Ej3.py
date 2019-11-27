num = int(input("Introdueix un numero enter positiu: "))  # Pedimos un numero
divsum = 0  # Iniciamos variable de la suma de divisores
num2 = 0  # Iniciamos el numero amigo
divsum2 = 0  # Iniciamos la variable de la suma de divisiores del numero amigo
while num <= 0:  # Comprobamos el numero
    print("¡Numero entero positivo!")  # Mostramos error
    num = int(input("Introdueix un numero enter positiu: "))
for i in range(1, num + 1):  # Iniciamos bucle
    if num % i == 0:  # Si i es divisora
        divsum += i  # Lo sumamos al resultado final
divsum -= num  # Hacemos calculo final
print("Suma divisores: ", divsum)  # Mostramos la suma de divisores menos su numero
while divsum2 != divsum:  # Iniciamos bucle hasta que se no se cumpla la condicion
    num2 = num2 + 1  # Sumamos 1 a numero amigo
    if num2 is num:  # Comprobamos que no sea el mismo numero
        num2 = num2 + 1  # Si lo es, sumamos 1
    divsum2 = 0  # Reseteamos la suma de sus divisores
    for i in range(1, num2 + 1):  # Iniciamos bucle
        if num2 % i == 0:  # Si i es divisora
            divsum2 += i  # Lo sumamos al resultado final
    divsum2 -= num2  # Hacemos calculo final
print(num2, " es numero amigo de ", num)  # Imprimimos numero amigo
print("Suma divisores numero amigo: ", divsum2)  # Imprimimos suma divisores numero amigo
