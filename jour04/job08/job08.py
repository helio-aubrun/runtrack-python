L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
s=0
i=0
for i in range(len(L)):
    if L[i]%2==0:
        s=s+L[i]
print (s)