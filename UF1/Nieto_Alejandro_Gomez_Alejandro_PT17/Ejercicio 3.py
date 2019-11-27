agenda = {"Alex": "679365974"}  # Iniciamos la variable con un contacto
while True:
    name = str(input("Introduce un nombre: "))  # Pedimos un valor
    if name in agenda:  # Comprobamos si el valor existe en la agenda
        print("Modificar el numero de ", name, end="")
        opc = str(input("1:SI"))
        if opc == '1':
            # Recojemos el telefono y lo sobreescribimos en sobre la llave que equivale al nombre
            print("Modificar telefono de: ", name, "(. Actual", agenda[name], "): ", end="")
            tlf = int(input())
            agenda[name] = tlf
    else:
        # Añadimos un telefono a la llave del nombre que no se encontraba en nuestra agenda
        print("Añadir telefono de ", name, ": ", end="")
        tlf = int(input())
        agenda[name] = tlf
    print(agenda)  # Mostramos el diccionario
    temp = str(input("Quieres continuar? *:NO"))
    if temp == '*':
        break
print(agenda)