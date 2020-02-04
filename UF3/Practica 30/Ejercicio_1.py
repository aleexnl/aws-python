tablets = open("Tablets.txt", "rt")
tablets2 = open("Tablets2.txt", "w")
while True:
    try:
        precio = float(input("Introduce el importe maximo que estas dispuesto a gastar:"))
        break
    except ValueError:
        print("Tienes que introducir numeros")
def tabletsBarats(nomf1, nomf2, p):
    lectura = nomf1.readlines()
    for lineas in lectura:
        lin = lineas.split(";")
        if float(lin[4]) <= p:
            escritura = lin[0][:3]+ "-"+ lin[1]+ "-"
            if int(lin[3]) > 900:
                escritura = escritura + "Alta" + "\n"
            if int(lin[3]) >= 500 and  int(lin[3]) <= 900:
                escritura = escritura + "Media" + "\n"
            if int(lin[3]) < 500:
                escritura = escritura + "Baja" + "\n"
            print("escribimos en fichero = ",escritura)
            nomf2.write(escritura)
tabletsBarats(tablets,tablets2,precio)
tablets.close()
tablets2.close()

