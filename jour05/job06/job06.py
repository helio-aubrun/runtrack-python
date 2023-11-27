def phare(nb_marche, cm):
    resultat=0
    m=cm/100
    for i in range(nb_marche):
        resultat=m
        i=i+1
    resultat=resultat*2
    resultat=resultat*5
    resultat=resultat*7
    print ("Pour ",nb_marche, " marches de ",cm, " le gardien parcourt ",resultat," m par semaine.")

phare (5,10)