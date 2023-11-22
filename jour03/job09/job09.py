def moyenne (n1, n2, n3):
    moyenne_etudiant=(n1+n2+n3)//3
    if 15<=moyenne_etudiant and moyenne_etudiant<=20:
        print ("Très bon élève")
    elif 11<=moyenne_etudiant and moyenne_etudiant<=14:
        print ("Bon élève")
    elif 8<=moyenne_etudiant and moyenne_etudiant<=10:
        print ("Elève moyen")
    else:
        print ("Elève devant faire des efforts")
    
moyenne(15,16,17)
moyenne(11,12,13)
moyenne(9,10,8)
moyenne(0,1,2)