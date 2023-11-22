def pair_impair (nb):
    if nb>0 and isinstance(nb, int):
        if nb%2==0:
            print ("pair")
        else:
            print ("impair")
    else:
        print ("erreur")

pair_impair (2)
pair_impair (3)
pair_impair (-2)
pair_impair (3.5)