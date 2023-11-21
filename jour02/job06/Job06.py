i=2
for i in range(7920):
    premier=True
    n=2
    while i>n and premier==True :
        if i%n==0 :
            premier=False
        n=n+1
    if premier:
        print (i)
    i=i+1