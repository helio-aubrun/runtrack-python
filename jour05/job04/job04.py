def colonne(n):
    print("+", end="")
    for i in range(n+1):
        print("-", end="")
        i=i+1
    print("+")
    a=0
    b=n
    c=0
    for a in range(n+1):
        print ("|", end="")
        for c in range(n+1):
            if c==b:
                print (" ", end="")
            else:
                print ("#", end="")
        print ("|")
        b=b-1
    i=0
    print("+", end="")
    for i in range(n+1):
        print("-", end="")
        i=i+1
    print("+", end="")
    
colonne(10)