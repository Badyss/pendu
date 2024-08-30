import time
import random

mots = ["affichage", "reste", "manger"]

def main(mot, affichage):
    affichage_mot = mot[0]
    for lettre in mot[1:]:
        if lettre in affichage:
            affichage_mot += lettre
        else:
            affichage_mot += "_"
    print(affichage_mot)
    
def jouer():
    mot = random.choice(mots)
    affichage = []
    erreurs = 0

    while True:
        main(mot, affichage)
        tentative = input("Choississez une lettre")
        if tentative in mot:
            if tentative in affichage:
                print("La lettre à déjà été trouvée")
            else:
                affichage.append(tentative)
                print("Trouvé !")
        else:
            erreurs += 1
            print("Non, tu as " + str(erreurs) + " erreurs.")
jouer()