L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
p=1
for i in range(len(L)):
    if 25<=L[i]<=90:
        p=p*L[i]
print (p)