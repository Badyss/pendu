import random

mots = ["affichage", "reste", "manger"]

def mot_trouve(mot, affichage):
    return all(lettre in affichage for lettre in mot)
    #On vérifie si toutes les lettres du mot sont présentes dans la liste affichage

def afficher_mot(mot, affichage):
    return ''.join(lettre if lettre in affichage else '_' for lettre in mot)

def jouer():
    mot = random.choice(mots)
    affichage = [mot[0]]
    erreurs = 0

    while True:
        print(afficher_mot(mot, affichage))

        if mot_trouve(mot, affichage):
            rejouer = input(f"Bravo, tu as gagné ! Le mot était '{mot}'. Veux-tu rejouer ? (oui/non) : ")
            if rejouer.lower() == "oui":
                jouer()
            else:
                print("D'accord, au revoir !")
            break

        tentative = input("Choisissez une lettre : ")
        if tentative in affichage:
            print("La lettre a déjà été trouvée.")
        elif tentative in mot:
            affichage.append(tentative)
            print("Trouvé !")
        else:
            erreurs += 1
            print(f"Non, tu as {erreurs} erreurs.")

jouer()
