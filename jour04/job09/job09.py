L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
max=0
min=9999999
i=0
for i in range(len(L)):
    if max<L[i]:
        max=L[i]
    elif min>L[i]:
        min=L[i]
print ("La valeur max est : ", max)
print ("la valeur min est : ", min)