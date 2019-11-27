# Iniciamos variables
suma = 0
total = 0
# Pedimos dia
day = int(input("Introduce el dia de nacimiento :"))
# Comprobamos que sea correcto
while day > 31 or day < 1:
    day = int(input("Introduce un dia valido (1-31): "))

# Pedimos mes
month = int(input("Introduce el mes de nacimiento :"))
# Comprobamos que sea correcto
while month > 12 or month < 1:
    month = int(input("Introduce un dia valido (1-12): "))

# Pedimos año
year = int(input("Introduce el año de nacimiento :"))
# Comprobamos que sea correcto
while year > 2019 or day < 1:
    year = int(input("Introduce un año valido (1-2019): "))

for i in str(day):
    suma = suma + int(i)

for i in str(month):
    suma = suma + int(i)

for i in str(year):
    suma = suma + int(i)

while suma >= 10:
    total = total+suma % 10
    suma = suma // 10
print("Numero de la suerte: ", suma)
