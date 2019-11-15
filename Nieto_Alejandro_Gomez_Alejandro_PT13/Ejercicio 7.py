sept = []
dic = []
dif = []
print("Alçada de septiembre: ")
for i in range(2):
    sept.append(float(input("Alçada "+str(i)+": ")))

for i in range(2):
    if sept[i] <= dic[i]:
        dic.append(float(input("Alçada "+str(i)+": ")))
    else:
        print("Alçada no valida no pot ferse mes petit")
        i=i-1
for i in range(len(sept)):
    dif.append(sept[i] - dic[i])

print("La lista de sepriembre és: "+ str(sept))
print("La lista de diciembre és: "+ str(dic))
print("La lista de las diferencias és: "+ str(dif))