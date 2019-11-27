# Iniciaremos el bucle directamente.
while True:
    # Esta es la creacion del menu
    print("CALCULADORA")
    print("Menu Principal")
    print(" ")
    print("1 - Sumar")
    print("2 - Restar")
    print("3 - Multiplicar")
    print("4 - Divir")
    print("0 - Sortir")

    #Se pide la opcion
    o=int(input("Escoje la opcion: "))
    #Y aqui estamos haciendo condicionales diciendo que si la opcion que han escojido es igual que a alguna opcion del menu se haga la operacion correspondiendiente, si no ha escojido ninguna de las opciones se le pondra campo no valido y que pueda volver a escojer alguna opcion.
    if o==1:
        #Se piden los dos numeros a operar
        num1=int(input("Introduce el primer valor: "))
        num2=int(input("Introduce el segundo valor: "))
        #Se hace la operacion escojida
        print(num1+num2)
        #Se pide que presione cualquier tecla para salir
        input("Presiona alguna tecla")
    elif o==2:
        # Se piden los dos numeros a operar
        num1 = int(input("Introduce el primer valor: "))
        num2 = int(input("Introduce el segundo valor: "))
        # Se hace la operacion escojida
        print(num1 - num2)
        # Se pide que presione cualquier tecla para salir
        input("Presiona alguna tecla")
    elif o==3:
        # Se piden los dos numeros a operar
        num1 = int(input("Introduce el primer valor: "))
        num2 = int(input("Introduce el segundo valor: "))
        # Se hace la operacion escojida
        print(num1 * num2)
        # Se pide que presione cualquier tecla para salir
        input("Presiona alguna tecla")
    elif o==4:
        # Se piden los dos numeros a operar
        num1 = int(input("Introduce el primer valor: "))
        num2 = int(input("Introduce el segundo valor: "))
        # Se hace la operacion escojida
        print(num1 / num2)
        # Se pide que presione cualquier tecla para salir
        input("Presiona alguna tecla")
    elif o==0:
        break
    else:
        print("Opcion no valida")
        input("Presiona alguna tecla")
print("Bye")
