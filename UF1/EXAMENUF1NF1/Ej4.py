num = int(input("Introduce un numero del 1 al 255: "))  # Pedimos valor
r = []  # Iniciamos una lista
while num > 255 or num < 1:  # Mientras cumpla estas condiciones
    print("¡Introduce un valor valido!")  # Mostramos error
    num = int(input("Introduce un numero del 1 al 255: "))  # Pedimos valor
while num >= 2:  # Mientras hayan posibles divisores
    r.append(int(num % 2))  # añadimos el numero divisor
    num = num / 2  # Dividimos nuestro numero
r.append(int(num))  # Añadimos el numero sea 0 o 1
r.reverse()  # Damos la vuelta al resultado
print(r)  # Mostramos el resultado
