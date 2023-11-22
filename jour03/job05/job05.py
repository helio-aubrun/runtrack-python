def calcule (n1,op,n2):
    if op=="+":
        return n1 + n2
    elif op=="-":
        return n1-n2
    elif op=="*":
        return n1*n2
    elif op=="/":
        return n1//n2
    elif op=="%":
        return n1%n2

print (calcule(1,"+",2))
print (calcule(2,"-",1))
print (calcule(2,"*",1))
print (calcule(2,"/",1))
print (calcule(2,"%",1))