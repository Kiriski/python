from random import *

rnum = randint(1, 10)









































trouve = False

while not trouve:  # l'utilisateur va chercher le juste prix a partir d'ici
    print("Entrez un chiffre :")
    propositionEnString = input()
    chi_pro = int(propositionEnString)

    trouve = chi_pro == rnum
    if not trouve:
        if rnum < chi_pro:
            print("Le chiffre mystère est plus petit")
        else:
            print("Le chiffre mystère est plus élevé")

print("Vous avez trouvé le bon chiffre")

