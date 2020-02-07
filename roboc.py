# -*- coding: utf8 -*-

"""Fichier éxécutant le jeu ROBOC en Python"""

import re
import os
from fonctions import *
from classe_robot import *
from classe_labyrinthe import *

# On affiche les choix de cartes disponibles
liste_des_cartes, liste = liste_des_cartes()
print(liste_des_cartes)

# On demande à l'utilisateur d'en choisir une
choix = choisir_carte(liste)

# On la récupère
carte = recup_carte(choix)
print(carte, "\n")

 # On crée l'objet labyrinthe
labyrinthe = Labyrinthe()
# On traite la carte pour la rendre exploitable
labyrinthe.crea_carte(carte)

# On crée notre objet Robot
robot = Robot()
# On récupère sa position initiale
robot.recup_position(labyrinthe.grille)

# On lance la partie
continuer = True
while continuer:
    # Demander à l'utilisateur la direction à prendre
    direction = input("Dans quelle direction doit-on aller :\n\
N pour aller au Nord, E pour Est, S pour Sud, O pour Ouest \n\
vous pouvez préciser le nombre de pas à effectuer (exemple: S3 ou N2) \n\
ou tapez Q pour sauvegarder et quitter la partie :\n ")

    # Vérifier la direction et lever une exception si nécéssaire
    try:
        expression = r"^[SNEOQsneoq]{1}[0-9]?$"
        if re.search(expression, direction) is None:
            raise ValueError
    except ValueError:
        print("\n La direction n'est pas valide !!\n")
        continue

    continuer, sortie = robot.action(direction, labyrinthe)
    # Sauvegarder
    labyrinthe.sauvegarder()
    # Si on trouve la sortie, on supprime la sauvegarde
    if sortie:
        labyrinthe.supprimer_sauvegarde()
