def username():  # Definimos funcion
    user = input("Introduce un nombre de usuario: ")  # Preguntamos nombre de usuario
    # Iniciamos el bucle que tiene que cumplir TODAS LAS CONDICIONES
    while len(user) < 6 or len(user) > 12 or str.isalpha(user) or str.isdigit(user) or str.isalnum(user) is False:
        if len(user) < 6:  # Si es menor que 6
            print("¡Tiene que tener al menos 6 caracteres")  # Muestra error
        if len(user) > 12:  # Si es mayor que 12
            print("¡No puede tener mas de 12 caracteres!")  # Muestra error
        if str.isalpha(user):  # Comprueba si es solo letra
            print("Debe contener al menos un numero")  # Muestra error
        if str.isdigit(user):  # Comprueba si es solo numero
            print("Debe contener al menos una letra")  # Muestra error
        if str.isalnum(user) is False:  # NO ES alfanumerico
            print("¡Solo puede y debe contener numeros y letras!")  # Muestra error
        else:
            user = input("Introduce un nombre de usuario: ")  # Vuelve a introducir
    print("Nombre de usuario valido.")  # Mostramos mensaje si cumplimos las condiciones


username()  # Llamamos a la funcion
