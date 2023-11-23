def tri(liste):
    index = 1
    try:
        while True:
            valeur_courante = liste[index]
            position = index

            while position > 0 and liste[position - 1] > valeur_courante:
                liste[position] = liste[position - 1]
                position = position - 1
            liste[position] = valeur_courante
            index += 1
    except IndexError:
        pass

ma_liste = [5, 2, 9, 1, 5, 6]
tri(ma_liste)
print(ma_liste)