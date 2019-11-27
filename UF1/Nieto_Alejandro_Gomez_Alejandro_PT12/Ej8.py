letrasdni = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X",
             "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]  # Iniciamos lista con valores pred.
dni = int(input("Introduce los numeros del DNI:"))  # Pedimos un DNI
while len(str(dni)) != 8:  # Comprobamos que tenga esta longitud bucle
    print("Introduce 8 numeros del DNI")  # Mensaje de error
    int(input("Introduce el DNI:"))  # Pedimos datos otra vez
calc = dni % 23  # Calculo de la letra en valor no ASCII
print("Tu DNI es: ", dni, end="")  # Mostramos mensaje
print(letrasdni[calc])  # de letra de DNI en la posicion de la lista

