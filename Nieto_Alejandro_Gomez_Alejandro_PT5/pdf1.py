# Preguntamos numero
x = float(input("Introduce tu numero: "))
# Iniciamos condicion
if x < 0:
    # Si es menor que 0, imprimimos valor absoluto
    print("Valor absoluto: ", abs(x))
else:
    # Cualuier otra cosa, imprimir el numero introducido
    print("Valor absoluto: ", x)
