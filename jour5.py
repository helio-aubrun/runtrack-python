# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 11:01:56 2023

@author: aubru
"""
#name=input()
#print('Hello ', name)

def draw_rectangle(width, height):
    for i in range(height):
        if i == 0 or i == height - 1:
            print("-" * width)
        else:
            print("|" + " " * (width-2) + "|")

#draw_rectangle(8, 6)

def afficher_tapis(n):
    for i in range(n+1):
        for j in range(n+1):
            if i == j:
                print(" ", end="")
            elif i + j == n:
                print(" ", end="")
            else:
                print("#", end="")
        print()
    print(" " * (n) + " ")

#afficher_tapis(5)

def message_codé(message, decalage):
    message_decale = ''
    for lettre in message:
        if lettre.isalpha():
            if lettre.isupper():
                nouvelle_lettre = chr((ord(lettre) - 65 + decalage) % 26 + 65)
            else:
                nouvelle_lettre = chr((ord(lettre) - 97 + decalage) % 26 + 97)
        else:
            nouvelle_lettre = lettre
        message_decale += nouvelle_lettre
    return message_decale

#print(message_codé('youpi c fait', 5))

def dist_wc(marches, hauteur):
    hauteur_m = hauteur / 100
    distance_marche = 2 * hauteur_m
    distance_totale = marches * distance_marche
    distance_totale += (marches - 1) * distance_marche
    distance_totale *= 7  
    distance_totale = round(distance_totale, 2)
    message = f"Pour {marches} marches de {hauteur} cm, le gardien parcourt {distance_totale} m par semaine."
    return message

#print(dist_wc(100, 50))

def arrondir_notes(notes):
    notes_arrondies = []
    for note in notes:
        if note < 40:
            notes_arrondies.append(note)
        else:
            multiple_de_5_suivant = (note // 5 + 1) * 5
            if multiple_de_5_suivant - note < 3:
                notes_arrondies.append(multiple_de_5_suivant)
            else:
                notes_arrondies.append(note)
    return notes_arrondies

#notes = [78, 62, 36, 91, 85, 49]
#notes_arrondies = arrondir_notes(notes)
#print(notes_arrondies)

def changer_mot(mot):
    if not mot.isalpha():
        print("Le mot doit contenir uniquement des lettres de l'alphabet")
        return mot
    liste_lettres = list(mot)
    index1 = None
    for i in range(len(liste_lettres) - 2, -1, -1):
        if liste_lettres[i] < liste_lettres[i+1]:
            index1 = i
            break
    if index1 is None:
        print("Le mot est déjà le plus grand dans l'ordre alphabétique")
        return mot
    index2 = None
    for i in range(len(liste_lettres) - 1, index1, -1):
        if liste_lettres[i] > liste_lettres[index1]:
            index2 = i
            break
    liste_lettres[index1], liste_lettres[index2] = liste_lettres[index2], liste_lettres[index1]
    liste_lettres[index1+1:] = reversed(liste_lettres[index1+1:])
    nouveau_mot = ''.join(liste_lettres)
    return nouveau_mot

