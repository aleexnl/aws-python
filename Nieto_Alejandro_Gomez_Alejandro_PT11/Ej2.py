def password():  # Definimos la funcion
    passwd = input("Introduce una contraseña: ")  # Pedimos la contraseña
    # Ponemos un bucle que se entrara siempre que se cumpla al menos una de las condiciones
    while len(passwd) < 8 or str.isupper(passwd) is True or str.islower(passwd) is True or str.isdigit(passwd) is True \
            or str.isalpha(passwd) is True or str.isalnum(passwd) is True or str.find(passwd, " ") is True:
        if len(passwd) < 8:  # Si es la contraseña mas corta que 8 caracteres
            print("Tiene que tener al menos 8 caracteres")  # Mostramos el error
        if str.isupper(passwd) is True:  # Si la contraseña es tot mayusculas
            print("Debe tener al menos una minuscula!")  # Mostramos el error
        if str.islower(passwd) is True:  # Si la contraseña es tot minusculas
            print("Debe contener al menos una mayuscula")  # Mostramos el error
        if str.isdigit(passwd) is True:  # Si la contraseña es tot digitos
            print("Debe contener al menos una letra")  # Mostramos error
        if str.isalpha(passwd) is True:  # Si la contraseña es tot letras
            print("Debe contener al menos un numero")  # Mostramos error
        if str.isalnum(passwd) is True:  # Si la contraseña es alfanumerica
            print("Debe contener un caracter especial")  # Mostramos error
        if passwd.find(" ") > 0:  # Si hay espacios en el contenido
            print("No puede contener espacios")  # Mostramos error
        else:  # Otra cosa...
            passwd = input("Introduce una contraseña: ")  # Permitimos volver a introducir
    print("Nombre de usuario valido.")  # Mostramos mensaje de usuario validado


password()  # Llamamos a la funcion
