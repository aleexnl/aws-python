# Pedimos datos
# Edad
age = int(input("Introduce tu edad: "))
# Ingresos familiares
igfam = float(input("Introduce los ingresos familiares: "))
# Numero de hermanos
bro = int(input("Introduce el numero de hermanos: "))

# Calculo disponible beca
if (bro*5700)+500 >= igfam:
    # Comprobar compensacion
    if bro > 4:
        print("Cantidad de beca: 150€")
    # Beca no disponible
    else:
        print("Beca no disponible")
# Beca disponible
elif (bro*5700)+500 < igfam:
    beca = (4000*(bro*5700)+500-igfam)/((bro*5700)+500)
    # Comprobar mayoria de edad
    if age < 18:
        # Si menor, incluir incremento
        print("Cantidad de beca: ", beca+(beca*0.1))
    else:
        # Imprimir beca
        print("Cantidad de beca: ", beca)
