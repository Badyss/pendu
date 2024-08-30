import time
import random

mots = ["affichage", "reste", "manger"]



def main(mot, affichage):
    caractères = len(mot)
    print(mot[0] + "_" * caractères + affichage)
    
def jouer():
    mot = random.choice(mots)
    affichage = [""]
    main(mot, affichage)

    erreurs = 0

    while True:
        tentative = input("Choississez une lettre")
        if tentative in mot:
            tentative.append(affichage)
            print("Trouvé !")
        else:
            erreurs += 1
            print("Non, tu as " + str(erreurs) + " erreurs.")
jouer()