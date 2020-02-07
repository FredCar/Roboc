# -*- coding: utf8 -*-

"""Fichier contenant la classe "Robot"
nécéssaires à l'éxecution du fichier roboc.py"""

import os
from classe_labyrinthe import *

class Robot:

    """Classe définissant notre robot"""

    def __init__(self):

        """Fonction d'initialisation"""

        self.x = 0
        self.y = 0
        self.avant = " "



    def recup_position(self, grille):

        """Fonction récupérant la position du robot représenté par 'X'"""

        # On itère dans le dico jusqu'à trouver X
        for x in grille:
            for y in grille[x]:
                if y == "X":
                    # On récupère les coordonnées de X
                    self.x = x
                    self.y = grille[x].index("X")

        return self.x, self.y



    def action(self, direction, labyrinthe):

        """Fonction réalisant les mouvements du robot"""

        # On récupère la direction et le nombre de pas à éffectuer
        if len(direction) == 2:
            pas = int(direction[1])
        else:
            pas = 1
        direction = direction[0]

        # Réafectation pour simplifier le nom
        grille = labyrinthe.grille
        i = 0
        while i < pas:
            # On se déplace à gauche : "colonne - 1"
            if direction.upper() == "O":

                # On vérifie les obstacles
                if grille[self.x][self.y - 1] == " " \
                   or grille[self.x][self.y - 1] == "." \
                   or grille[self.x][self.y - 1] == "U":

                    # Après le mouvement, on remplace X
                    # Soit par du vide, soit par ce qu'y trouvé avant
                    grille[self.x][self.y] = self.avant

                    # On calcule la nouvelle position de X
                    self.y -= 1

                    # On mémorise ce qui se trouve là ou va X
                    self.avant = grille[self.x][self.y]

                    # On déplace X
                    grille[self.x][self.y] = "X"

                else:
                    print("\n Il y a un obstacle !!")


            # On se déplace à droite : "colonne + 1"
            if direction.upper() == "E":

                # On vérifie les obstacles
                if grille[self.x][self.y + 1] == " " \
                   or grille[self.x][self.y + 1] == "." \
                   or grille[self.x][self.y + 1] == "U":

                    # Après le mouvement, on remplace X
                    # Soit par du vide, soit par ce qu'y trouvé avant
                    grille[self.x][self.y] = self.avant

                    # On calcule la nouvelle position de X
                    self.y += 1

                    # On mémorise ce qui se trouve là ou va X
                    self.avant = grille[self.x][self.y]

                    # On déplace X
                    grille[self.x][self.y] = "X"

                else:
                    print("\n Il y a un obstacle !!")


            # On se déplace en haut : "ligne - 1"
            if direction.upper() == "N":

                # On vérifie les obstacles
                if grille[self.x - 1][self.y] == " " \
                   or grille[self.x - 1][self.y] == "." \
                   or grille[self.x - 1][self.y] == "U":

                    # Après le mouvement, on remplace X
                    # Soit par du vide, soit par ce qu'y trouvé avant
                    grille[self.x][self.y] = self.avant

                    # On calcule la nouvelle position de X
                    self.x -= 1

                    # On mémorise ce qui se trouve là ou va X
                    self.avant = grille[self.x][self.y]

                    # On déplace X
                    grille[self.x][self.y] = "X"

                else:
                    print("\n Il y a un obstacle !!")


            # On se déplace en bas : "ligne + 1"
            if direction.upper() == "S":

                # On vérifie les obstacles
                if grille[self.x + 1][self.y] == " " \
                   or grille[self.x + 1][self.y] == "." \
                   or grille[self.x + 1][self.y] == "U":

                    # Après le mouvement, on remplace X
                    # Soit par du vide, soit par ce qu'y trouvé avant
                    grille[self.x][self.y] = self.avant

                    # On calcule la nouvelle position de X
                    self.x += 1

                    # On mémorise ce qui se trouve là ou va X
                    self.avant = grille[self.x][self.y]

                    # On déplace X
                    grille[self.x][self.y] = "X"

                else:
                    print("\n Il y a un obstacle !!")

            # L'utilisateur a décidé de quitter la partie
            if direction.upper() == "Q":
                continuer = False
                sortie = False
                labyrinthe.afficher_carte()

                return continuer, sortie

            # On vérifie si la sortie est atteinte
            if self.avant == "U":
                labyrinthe.afficher_carte()
                print("\n Bravo, vous avez trouvé la sortie !!\n")
                continuer = False
                # On supprime la sauvegarder
                sortie = True

                return continuer, sortie

            labyrinthe.afficher_carte()
            i += 1

        continuer = True
        sortie = False
        return continuer, sortie
