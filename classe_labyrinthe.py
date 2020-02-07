# -*- coding: utf8 -*-

"""Fichier contenant la classe "labyrinthe"
nécéssaires à l'éxecution du fichier roboc.py"""

import os

class Labyrinthe:

    """Classe définissant le labyrinthe"""
    
    def __init__(self):

        """Initialisation du labyrinthe"""

        self.grille = {}
        self.affichage = ""


    def crea_carte(self, carte):

        """Fonction décomposant le modèle pour le rendre exploitable"""

        # On crée une liste contenant chaques lignes de la carte
        lignes = carte.split("\n")

        # On rempli le dictionnaire grille
        # avec chaques caractères pour chaques lignes
        i = 0
        for l in lignes:
            cle = i
            self.grille[cle] = []
            i += 1

            for c in l:
                self.grille[cle].append(c)

        return self.grille



    def afficher_carte(self):

        """Méthode recalculant et affichant la carte après les mouvements"""

        self.affichage = ""
        for ligne in self.grille:
            self.affichage += "\n"
            for col in self.grille[ligne]:
                self.affichage += col

        self.affichage += "\n"
        print(self.affichage)

        return self.affichage



    def sauvegarder(self):

        """Méthode de sauvegarde"""

        with open("cartes/sauvegarde.txt", "w") as fichier:
            fichier.write(self.affichage)



    def supprimer_sauvegarde(self):

        """Fonction supprimant la sauvegarde"""

        os.remove("cartes/sauvegarde.txt")
