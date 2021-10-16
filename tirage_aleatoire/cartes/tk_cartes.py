#-------------------------------------------------------------------------------
# Name:        module1
# Author:      h
# Created:     31/05/2021
#-------------------------------------------------------------------------------
# -*- coding: UTF-8 -*-

from tkinter import *
from random import shuffle, randint, choice
import cartes as CARTES


#--- Programme principal -------------------------------------------------------


def carte():
    global carte1

    #appel de la méthode
    jeu.Afficher_une_carte()

    # Une carte à afficher
    carte1 = Text(frame1, bg="yellow", fg="black", font=("Courier", 9, "bold"),
    height=1, width=17,padx=12)
    carte1.place(relx=0.04, rely=0.7)

    # attribut
    carte1.insert(END, jeu.tirer_une_carte)
##    carte1 = jeu.tirer_une_carte
##    # label qui affiche une carte
##    carte_label = Label(frame1, bg="yellow", fg="black", font=("Courier", 11, "bold"),
##    text=carte1)
####    carte_label.grid(row=3, column=0, sticky=N)
##    carte_label.place(relx=0.09, rely=0.7)

def melanger():

    global paquet1, paquet2

    #appel de la méthode
    jeu.Melanger()

    # variable d'instance assignée à paquet représant la liste 52 cartes
    jeu.melanger





##    #afficher le paquet de cartes
##    paquet_label = Label(frame1, text="liste 52 cartes" , bg="yellow", fg="red")
##    paquet_label.grid(row=0, column=1)

    # affichage de la liste 52 cartes dans widget Text
    paquet1 = Text(frame1, bg="orange", height= 27, width=20)
##    paquet1.grid(row=0, rowspan=3, column=1)
    paquet1.place(relx=0.4, rely=0)

    paquet2 = Text(frame1, bg="orange", height=27, width=20)
##    paquet2.grid(row=0, rowspan=3, column=2)
    paquet2.place(relx=0.7, rely=0)

    count = 0
    for i in jeu.melanger:
        if count % 2 != 0:
            paquet1.insert(END, i+"\n")
        else:
            paquet2.insert(END, i+"\n")
        count += 1




if __name__ == '__main__':

    #création d'une fenêtre Tk
    fenetre = Tk()
    fenetre.geometry("550x430")
    fenetre.title("Jeu de 52 cartes")
    fenetre.config(bg="yellow")

    #création d'une frame
    frame1 = Frame(fenetre, bg="orange")
    ##frame1.grid()
    frame1.place(relx=0,rely=0, height=430, width=450)


    #instanciation
    jeu = CARTES.Jeu_cartes52()

    #MELANGER - BOUTON

    #création du BOUTON mélanger - grid et placeZ
    melanger_bt = Button(frame1, text="Mélanger", bd=4, bg="yellow", command=melanger)
##    melanger_bt.grid(row=0, column=0, padx=10, pady=10)
    melanger_bt.place(relx=0.13, rely=0.25)



    #TIRER UNE CARTE - BOUTON

    #création du BOUTON tirage d'une carte - grid et place
    carte_bt = Button(frame1, text="Tirer une carte", bd=5,bg="yellow", command=carte)
##    carte_bt.grid(row=1, column=0, padx=10, pady=10, sticky=S)
    carte_bt.place(relx=0.1,rely=0.5)



    fenetre.mainloop()



