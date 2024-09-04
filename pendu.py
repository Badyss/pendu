import random

mots = ["affichage", "reste", "manger"]

def mot_trouve(mot, affichage):
    for lettre in mot:
        if lettre not in affichage:
            return False
    return True

def main(mot, affichage):
    if mot_trouve(mot, affichage):
        rejouer = input("Bravo tu as gagné, veux-tu rejouer ? (oui/non) : ")
        if rejouer.lower() == "oui":
            jouer()
        else:
            print("D'accord, au revoir !")
            return True 
    else:
        affichage_mot = mot[0]
        for lettre in mot[1:]:
            if lettre in affichage:
                affichage_mot += lettre
            else:
                affichage_mot += "_"
        print(affichage_mot)
    return False

def jouer():
    mot = random.choice(mots)
    affichage = []
    erreurs = 0

    while True:
        if main(mot, affichage):
            break
        tentative = input("Choisissez une lettre : ")
        if tentative in mot:
            if tentative in affichage:
                print("La lettre a déjà été trouvée.")
            else:
                affichage.append(tentative)
                print("Trouvé !")
        else:
            erreurs += 1
            print("Non, tu as " + str(erreurs) + " erreurs.")

jouer()