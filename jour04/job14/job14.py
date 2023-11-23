def my_long_word(longueur_min, chaine):
    mots = ""
    mot_actuel = ""
    for caractere in chaine:
        if caractere.isalpha():
            mot_actuel += caractere
        elif mot_actuel != "":
            if len(mot_actuel) > longueur_min:
                mots += mot_actuel + " "
            mot_actuel = ""
    if len(mot_actuel) > longueur_min:
        mots += mot_actuel
    return mots

resultat = my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")
print(resultat)