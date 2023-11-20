def contient_e(chaine):
    if 'e' in chaine:
        return True
    else:
        return False

chaine = input("Entrez une chaîne de caractères : ")
resultat = contient_e(chaine)

if resultat:
    print("La chaîne contient le caractère 'e'.")
else:
    print("La chaîne ne contient pas le caractère 'e'.")