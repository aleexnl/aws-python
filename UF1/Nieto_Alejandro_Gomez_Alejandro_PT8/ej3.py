print("REPETICIONES")
print(" ")
enter=int(input("Escriu un numero enter: "))
cantidad=int(input("Quants numeros vas a introduir: "))
contador=0
contadorenter=0
while True:
    contador=contador+1
    num=int(input("Esriu un numero enter: "))
    if num==enter:
        contadorenter=contadorenter+1
    if contador==cantidad:
        break
if contadorenter>cantidad/2:
    print("Has escrit mes vegades el número "+str(enter)+" que la resta de numeros")
elif contadorenter<cantidad/2:
    print("Has escrit menys vegades el número "+str(enter)+" que la resta de numeros")
else:
    print("Has escrit tantes vegades el número "+str(enter)+" com la resta de numeros")
