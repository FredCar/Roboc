# -*- coding: utf8 -*-

"""Fichier contenant les fonctions nécéssaires
à l'éxécution du fichier roboc.py"""

from classe_robot import *
import os
import re

def liste_des_cartes():

    """Fonction listant les cartes disponibles"""

    # On récupère la liste des fichiers du dossier "cartes"
    liste = os.listdir("cartes/")

    # On prépare la chaine qui liste les cartes disponibles
    liste_des_cartes = "Labyrinthes existants :\n"
    i = 1
    for x in liste:
        # On ne veut pas afficher le .DS_STORE
        if x[0] != ".":
            liste_des_cartes += str(i) + " - " + x[:-4] + "\n"
        i += 1

    return liste_des_cartes, liste



def choisir_carte(liste):

    """Fonction demandant à l'utilisateur de choisir une carte"""

    ok = True
    while ok:
        choix = input("Choisissez le numéro d'une carte : \n")

        # Gérer les exceptions
        try:
            expression = r"^[1-9]{1}$"
            if re.search(expression, choix) is None:
                raise ValueError
        except ValueError:
            print("\n Choix non valide !!\n")
            continue

        try:
            choix = int(choix)
        except ValueError:
            print("\n Choix non valide !!\n")
            continue

        try:
            choix = liste[choix - 1]
            print(choix)
        except IndexError:
            print("\n Choix non valide !!\n")
            continue

        ok = False

    return choix



def recup_carte(choix):

    """Fonction récupérant la carte dans le dosiers stockant les modèles"""

    adresse = "cartes/" + str(choix)

    # On récupère la carte choisie dans le dossier
    with open(adresse, "r") as fichier:
        carte = fichier.read()

    return carte
