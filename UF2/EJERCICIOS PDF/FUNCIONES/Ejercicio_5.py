"""Creeu una funció “esDigit” que, donat un caràcter qualsevol, ens digui si és numèric o no. La funció rep un paràmetre
 que representarà un únic caràcter, i retorna un valor entero ( 1 si el caràcter és un número, 0 si no ho és)."""


def esdigito(text):
    if text.isdigit() is True:
        print("1")
    elif text.isdigit() is False:
        print("0")
    else:
        print("Error no esperado")


var1 = str(input("Introduce 1 valor: "))
while len(var1) != 1:
    print("¡La longitud de la cadena tiene que ser 1!")
    var1 = str(input("Introduce 1 valor: "))
esdigito(var1)
