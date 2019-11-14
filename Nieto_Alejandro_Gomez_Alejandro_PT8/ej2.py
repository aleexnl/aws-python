# Pedimos numero
m = int(input("Escriu la grandària del segment: "))
# Mientras el numero no funcione,
# pediremos uno hasta que sea valido
while m < 0:
    print("No has escritu un número enter positiu")
    m = int(input("Escriut la grandària del segment: "))
# Pedimos numero
n = int(input("Escriu el número de segments: "))
# Mientras el numero no funcione,
# pediremos uno hasta que sea valido
while n < 0:
    print("No has escritu un número enter positiu")
    n = int(input("Escriu el número de segments: "))

# Repetimos tantas veces el print
# como nos han indicado en n
for i in range(n):
    # Imprime m asteriscos como se ha indicado
    print("*" * m, end="\t")
