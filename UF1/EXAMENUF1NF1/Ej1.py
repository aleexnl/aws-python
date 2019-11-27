saldo = int(1000)  # Iniciamos la variable con cantidad fija
while True:
    print("CAIXER <<NOM DEL CAIXER>>")  # Mostramos el menu por pantalla
    print("1 - Retirar Efectiu")
    print("2 - Ingressar")
    print("3 - Consultar saldo")
    print("4 - Sortir")
    opc = int(input("Introdueix una opcio: "))  # Pedimos una opcion
    while opc > 4 or opc < 1:  # Comprobamos la opcion
        print("Opcion no valida")  # Mostramos error
        opc = int(input("Introdueix una opcio: "))
    if opc is 1:  # Opcion 1
        wdraw = int(input("Introduce cantidad a retirar: "))  # Pedimos cantidad a retirar
        while wdraw > saldo:  # Comprobamos que sea valida
            print("No puedes retirar ese dinero!")  # Mensaje error
            wdraw = int(input("Introduce cantidad a retirar: "))
        while wdraw < 1:
            print("No puedes retirar ese dinero!")  # Mensaje error
            wdraw = int(input("Introduce cantidad a retirar: "))
        saldo -= wdraw  # Calculo saldo - dinero retirado
        print("Saldo actual: ", saldo)  # Mostramos saldo
        input("Pulsa cualquier tecla para volver al menu")  # Tecla para volver al menu
    if opc is 2:  # Opcion 2
        deposit = int(input("Introduce cantidad a depositar: "))  # Pedimos cantidad a retirar
        while deposit <= 0:  # Comprobamos que sea valida
            print("¡Ingresa una cantidad minima de 1€!")  # Mensaje error
            deposit = int(input("Introduce cantidad a depositar: "))
        saldo += deposit  # Calculo saldo + dinero ingresado
        print("Saldo actual: ", saldo)  # Mostramos saldo
        input("Pulsa cualquier tecla para volver al menu")  # Tecla para volver al menu
    if opc is 3:  # Opcion 3
        print("Saldo actual: ", saldo)  # Mostramos saldo
        input("Pulsa cualquier tecla para volver al menu")  # Tecla para volver al menu
    if opc is 4:  # Opcion 4
        print("¡Hasta la proxima!")
        break  # Salimos del programa
