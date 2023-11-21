def triangle_type(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Les longueurs peuvent former un triangle.")
        if a == b == c:
            print("Le triangle est équilatéral.")
        elif a == b or a == c or b == c:
            if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
                print("Le triangle est rectangle et isocèle.")
            else:
                print("Le triangle est isocèle mais non rectangle.")
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Le triangle est rectangle.")
        else:
            print("Le triangle est quelconque.")
    else:
        print("Les longueurs ne peuvent pas former un triangle.")

a = float(input("Entrez la longueur a : "))
b = float(input("Entrez la longueur b : "))
c = float(input("Entrez la longueur c : "))
triangle_type(a, b, c)