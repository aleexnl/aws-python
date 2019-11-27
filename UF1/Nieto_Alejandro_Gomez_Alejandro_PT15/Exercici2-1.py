# Fem una tupla que emmagatzemi els ultims numeros de cada mes. I demanem les tres variables
dias_mes = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
anno = int(input("Dame un año: "))
mes = int(input("Dame un mes: "))
dia = int(input("Dame un dia: "))
# Si els dies son iguals a els dies del mes a la posicio -1
if dia == dias_mes[mes -1]:
    if mes == 12: # I a part el mes es igual a 12
        print("El dia seguent de (",anno, mes, dia,") és (",anno + 1, 1, 1,")") # Printarem el seguent

    else: # La reesta de mesos
        print("El dia seguent de (", anno, mes, dia, ") és (", anno, mes + 1, 1, ")") # Printarem aixo altra
# Si es el dia sumem un.
else: # I si es diferent al condicional de adalt
    print("El dia seguent de (", anno, mes, dia, ") és (", anno, mes, dia + 1, ")") # Printem aixó de aqui