# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 10:00:43 2023

@author: aubru
"""

import random

L = []
for i in range (5):
    L.append(random.randint(0,100))
    
#print(L[1])

def l3(liste):
    liste[3]=liste[2]+liste[4]
    return liste
    
#print(l3(L))
#print(L[4])

def grand_remplacement(liste):
    l=0
    l=liste[0]
    liste[0]=liste[len(liste)-1]
    liste[len(liste)-1]=l
    return liste

#print (L)
#print (grand_remplacement(L))

def compte(liste):
    occ=0
    for i in range(len(liste)):
        if liste[i]%3==0:
            occ=occ+1
    return occ 

l=[8,24,48,2,16]
#print(compte(l))

def somme_paire(liste):
    somm=0
    for i in range(len(liste)):
        if liste[i]%2==0:
            somm=somm+liste[i]
    return somm

#print(somme_paire(l))

def max_min(liste):
    maxi=0
    mini=100000000000000000000000000000000000000000000000000000000000000000000
    for i in range(len(liste)):
        if liste[i] < mini:
            mini=liste[i]
        if liste[i] > maxi:
            maxi=liste[i]
    return maxi, mini

L2=[8,24,27,48,2,16,9,102,7,84,91]
#print(max_min(L2))

def produit(liste):
    produit=1
    for i in range(len(liste)): #bonus : for i in range(4)
        if liste[i] <= 90 and liste[i] >= 25:
            produit=produit*liste[i]
    return produit

#print(produit(L2))

def plus_un(liste):
    for i in range(len(liste)):
        liste[i]=liste[i]+1
    return liste

L3=[7,11,42,39,2]
#print(plus_un(L3))

def croissant(liste):
    liste.sort()
    return liste
    
#print(croissant(L3))   

def doublon(liste):
    croissant(liste)
    i=1
    while i < len(liste):
        if liste[i]==liste[i-1]:
            del liste[i]
        i=i+1
    return liste

L4=[10,20,30,20,10,50,60,40,80,50,40]
#print(doublon(L4))

def my_long_word(chaine, n):
    liste_mots = chaine.split()
    mots_plus_longs = []
    for mot in liste_mots:
        if len(mot) > n:
            mots_plus_longs.append(mot)
    return mots_plus_longs

#print(my_long_word('La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance',3 ))   
      
def arrondir(liste):
    for i in range(len(liste)):
        liste[i]=round(liste[i])
    liste.sort()
    return liste

L6=[22.4, 4.0,16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
#print(arrondir(L6))