# Fem una tupla amb els dias que tenen cada mes
dias_mes = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# Fem una altra on passarem una data.
avui = (2018, 4, 11)
# Guardamos los valores de la tupla en las variables a(any), m(mes) y d(dia)
a, m, d = avui
# Creem una tupla a la cual possarem el dia que es nadal (25 de desdembre)
nadal = (2018, 12, 25)
# Guardamos los valores de la tupla en las variables a1, m1 y d1 (com en la tupla de abans)
a2, m2, d2 = nadal
# Creem una variable on guardarem el dia de nadal mes la suma de las resta dels dias del mes menys la data actual
suma = d2 + (dias_mes[m-1] -d)
# Finalment farem un bucle on guardarem en una variable la quantiat de dias que queden fins nadal i els printarem
for i in range(m, m2-1):
    suma = suma + dias_mes[i]
print("El dies entre avui i nadal són:", suma)

