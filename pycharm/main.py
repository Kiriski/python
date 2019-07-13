


def estBissextile1():
    annee = input("1 - Saisissez une année : ")
    annee = int(annee)
    bissextile = False
    if annee % 400 == 0:
        bissextile = True
    elif annee % 100 == 0:
        bissextile = False
    elif annee % 4 == 0:
        bissextile = True
    else:
        bissextile = False
    if bissextile:
        print("L'année saisie est bissextile.")
    else:
        print("L'année saisie n'est pas bissextile.")



def estBissextile2():
    annee = input("2 - Saisissez une année : ")  # On attend que l'utilisateur saisisse l'année qu'il désire tester
    annee = int(annee)  # Risque d'erreur si l'utilisateur n'a pas saisi un nombre

    if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
        print("L'année saisie est bissextile.")
    else:
        print("L'année saisie n'est pas bissextile.")



def estBissextile3():
    annee = input("3 - Saisissez une année : ")  # On attend que l'utilisateur saisisse l'année qu'il désire tester
    annee = int(annee)  # Risque d'erreur si l'utilisateur n'a pas saisi un nombre
    estX4 = annee % 4 == 0
    estX100 = annee % 100 == 0
    estX400 = annee % 400 == 0
    estBissextile = (estX4 and not estX100) or estX400
    if estBissextile:
        print("L'année saisie est bissextile.")
    else:
        print("L'année saisie n'est pas bissextile.")





estBissextile1()



