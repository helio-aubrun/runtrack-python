i=1
while i<101:
    if i%3==0:
        if i%5==0:
            print ("FizzBuzz")
        else:
            print ("Fizz")
    elif i%5==0:
        print ("Buzz")
    else:
        print(i)
    i=i+1