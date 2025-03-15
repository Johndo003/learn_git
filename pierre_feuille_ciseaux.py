# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 18:57:16 2025

@author: hp
"""

import random

def coup_to_str(coup):
    return ["PIERRE", "FEUILLE", "CISEAUX"][coup]

def jouer_manche(coup_joueur):
    coup_ordi = random.randint(0, 2)
    
    if coup_joueur == coup_ordi:
        
        result = f"{coup_to_str(coup_ordi)} annule {coup_to_str(coup_joueur)} : 1 point chacun"
        score = 0
        
    elif (coup_joueur == 0 and coup_ordi == 2) or (coup_joueur == 1 and coup_ordi == 0) or (coup_joueur == 2 and coup_ordi == 1):
        result = f"{coup_to_str(coup_ordi)} est battu par {coup_to_str(coup_joueur)} : 1 point pour le joueur"
        score = 1
    else:
        result = f"{coup_to_str(coup_ordi)} bat {coup_to_str(coup_joueur)} : 1 point pour l'ordinateur"
        score = -1
    return result, score

def jeu():
    """Joue cinq manches de Pierre-feuille-ciseaux et affiche le résultat final"""
    score_joueur = 0
    for i in range(5):
        while True:
            try:
                coup_joueur = int(input("Entrez votre coup (0: PIERRE, 1: FEUILLE, 2: CISEAUX): "))
                if coup_joueur in [0, 1, 2]:
                    break
                else:
                    print("Veuillez entrer un nombre entre 0 et 2.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")
        
        result, score = jouer_manche(coup_joueur)
        print(result)
        score_joueur += score
    
    if score_joueur > 0:
        print("Gagné")
    elif score_joueur < 0:
        print("Perdu")
    else:
        print("Nul")

# Démarrer le jeu
jeu()
