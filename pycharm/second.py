


def estBissextile1(annee):
    bissextile = False
    if annee % 400 == 0:
        bissextile = True
    elif annee % 100 == 0:
        bissextile = False
    elif annee % 4 == 0:
        bissextile = True
    else:
        bissextile = False
    return bissextile



def estBissextile2(annee):
    return annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0)



def estBissextile3(annee):
    estX4 = annee % 4 == 0
    estX100 = annee % 100 == 0
    estX400 = annee % 400 == 0
    estBissextile = (estX4 and not estX100) or estX400
    return estBissextile



annee = input("opti - Saisissez une année : ")  # On attend que l'utilisateur saisisse l'année qu'il désire tester
annee = int(annee)  # Risque d'erreur si l'utilisateur n'a pas saisi un nombre

resultat1 = estBissextile1(annee)
resultat2 = estBissextile2(annee)
resultat3 = estBissextile3(annee)

if resultat1:
    print("L'année saisie est bissextile.")
else:
    print("L'année saisie n'est pas bissextile.")



