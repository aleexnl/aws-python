# Iniciamos variable
contador = 0
# Pedimos valor
num = int(input("Introduce un multiplo de 10: "))

# Comprobamos valor,
# si es erroneo lo pedimos hasta que sea valido
while num % 10 != 0:
    print("No es valido, vuelve a intentar")
    num = int(input("Introduce un multiplo de 10: "))
# Iniciamos bucle;
# mientras se cumpla la condicion se ejecutara
# un contador
while num % 10 == 0:
    contador = contador + 1
    num = num // 10
# Mostramos resultado
print(num, " per 10 elevat a ", contador)
