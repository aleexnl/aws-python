#Definimos la variable tiempo que cuando entremos en el bucle es a la que iremos sumando 3
temps=0
# Esta variable es la cantidad que necesita un ser vivo para morirse por las bacterias.
need=10000000
# Y en esta ultima definimos que hay una bacteria en el ser vivo.
actual=1
# Si la bacteria/s actual es mas pequeña que las que se necesitan para morir entraremos en el bucle
while actual<need:
    # Aqui sumamos en cada vuelta del bucle 3 minutos
    temps=temps+3
    # Y aqui en cada vuelta multiplicaremos por 2 la bacteria/s por que cada 3 minutos cada una de ellas se duplica
    actual=actual*2
#Finalmente si no a entrado en el bucle significa que las bacterias actuales han llegado al a la cifra mortal y printaremos el tiempo.
print(str(temps)+" minuts tardara en assolir la xifra mortal")


