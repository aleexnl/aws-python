# Escriure el codi de la funció que imprimeixi per pantalla tants asteriscs como indiqui el número que rep com argument.
def printasteriscos(x):  # Definimos la funcion
    """Este bucle lo que hara es imprimir tantos asteriscos como en la variable indica"""
    for i in range(x):  # Iniciamos bucle
        print("*", end="")  # Printamos *, continuado del siguiente print


qty = int(input("Introduce la cantidad de asteriscos a imprimir: "))  # Pedimos un valor integro
printasteriscos(qty)  # Llamamos a la funcion y le apsamos los argumentos
