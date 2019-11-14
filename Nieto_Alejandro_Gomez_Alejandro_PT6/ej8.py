# Pedimos numero
num = int(input("Escriba un numero: "))

# Imprimimos los divisores continuados del for
print(f"Los divisores de {num} son ", end="")

# Iniciamos bucle
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
