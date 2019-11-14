# Pedimos una cadena
cadena=input("Dime una frase con o sin numero: ")
# Iniciamos la variable digit a false
digit=False
# Decimos que la I vaya comparando letra por letra si el ASCI de la letra que sea I en ese momento esta en el rango de 49 y 57 (estos incluidos) y si es el caso que DIGIT se combierta en true y se salga del bucle
for i in cadena:
    if ord(i) >= 49 and ord(i) <= 57:
        digit=True
        break
# Decimos si digit es true printe que si que tiene un digito y que sino es True que printe que no tiene.
if digit==True:
    print("Conte digit")
else:
    print("No conte digit")
