num = 0  # Iniciamos la variable numero
lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
         "v", "w", "x", "y", "z"]  # Iniciamos la lista con nuestros valores string
while num <= 9:  # Entramos al bucle mientras sea menor o igual a 9
    for i in range(len(lista)):  # Entramos a bucle
        a = (num, lista[i])  # Asignamos valor numero + valor lista segun posicion del bucle
        print(a)  # Printamos dupla de numero + contenido lista segun posicion
    num += 1  # Sumamos 1 a numero
