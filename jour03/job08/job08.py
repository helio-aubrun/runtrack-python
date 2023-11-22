def manger_5_fruits_et_legumes_par_jour (type, saison):
    if type=="fruits":
        if saison=="hiver":
            print ("orange, mandarine et kiwi")
        elif saison=="ete":
            print ("Poire, fraise, cassis")
        else:
            print ("jsp")
    elif type=="legume":
        if saison=="hiver":
            print ("carotte, topinambour, endive")
        elif saison=="ete":
            print ("artichaut, aubergine,navet")
        else:
            print ("jsp")
    else:
        print ("jsp")

manger_5_fruits_et_legumes_par_jour ("fruits", "hiver")
manger_5_fruits_et_legumes_par_jour ("fruits", "ete")
manger_5_fruits_et_legumes_par_jour ("legume", "hiver")
manger_5_fruits_et_legumes_par_jour ("legume", "ete")