import time
import random

mots = ["affichage", "reste", "manger"]



def main(mot, affichage):
    caractères = len(mot)
    for lettre in mot:
        if lettre in affichage:
            print(lettre)
        else:
            print("_")
    
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