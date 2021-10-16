#-------------------------------------------------------------------------------
# Name:        module1
# Author:      h
# Created:     31/05/2021
#-------------------------------------------------------------------------------
# -*- coding: UTF-8 -*-

from random import shuffle, randint, choice




#--- Programme principal -------------------------------------------------------

class Cartes():
    """Construit les 52 cartes"""
    def __init__(self):
        self.valeurs = ["As","Roi","Dame","Valet","10","9","8","7","6","5","4",
        "3","3"]
        self.couleurs = ["coeur","trèfle","pique","carreau"]
        #création de la liste 52 cartes
        self.cartes52 = []
        for figure in self.valeurs:
            for couleur in self.couleurs:
                fig = figure + " de " + couleur
                self.cartes52.append(fig)

class CartesJoker(Cartes):
    """Classe qui ajoute deux jokers aux 52 cartes
    Héritage de la classe Cartes"""

    # constructeur
    def __init__(self):

        # Héritage
        Cartes.__init__(self)
        self.joker = ["Joker"]
        self.cartes52.extend(self.joker*2)




class Jeu_cartes54(CartesJoker):
    """Tirer et afficher une carte dans un paquet de 52 cartes"""
    #constructeur
    def __init__(self):
        #héritage
        CartesJoker.__init__(self)
        self.tirer_une_carte = choice(self.cartes52)


    #méthode mélanger
    def Melanger(self):
        count = []
        self.melanger = []
        index = randint(0, len(self.cartes52)-1)
        # création d'une liste de cartes mélangées
        for i in range(0, len(self.cartes52)):
            while index in count:
                index = randint(0, len(self.cartes52)-1)
            else:
                self.melanger.append(self.cartes52[index])
                count.append(index)
        print("les {} cartes sont mélangées.\n".format(len(self.melanger)))
        return self.melanger

    # méthode affichage
    def Afficher_une_carte(self):
        self.tirer_une_carte = choice(self.melanger)
        print("Vous avez choisi la carte : {}".format(self.tirer_une_carte))
        return self.tirer_une_carte


if __name__ == '__main__':

    cartes = Cartes()
    print("Les valeurs :",cartes.valeurs, end="\n\n")
    print("Les couleurs :", cartes.couleurs, end="\n\n")

    #instanciation du jeu de cartes
    jeu = Jeu_cartes54()

    print("Tirer une carte :",jeu.tirer_une_carte)


    #attention appeler la méthode
    jeu.Melanger()

    jeu.Afficher_une_carte()

    joker=CartesJoker()
    print(joker.joker)
    #affichage des 52 cartes et des 2 jokers
    print(joker.cartes52)


