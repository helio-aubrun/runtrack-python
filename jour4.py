
fruits=["pomme","cerise","orange"]

def liste_fruit():
    return fruits

#print(liste_fruit())

def fruit2():
    print(fruits[1])
    
#fruit2()

def ajoute_melon():
    fruits.append('melon')
    
ajoute_melon()
#print(fruits)

def ajoute_mangue():
    fruits.insert(2,"mangue")
    
ajoute_mangue()
#print(fruits)