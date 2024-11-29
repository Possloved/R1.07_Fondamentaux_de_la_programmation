def taille(T):
    taille = 0
    while T[taille] != '\0':
        taille += 1
    return taille
def pourcentage_voyelles(T):
    voyelles = "aeiouAEIOU"
    nb_voyelles = 0
    taille_T = taille(T)
    for i in range(taille_T):
        if T[i] in voyelles:
            nb_voyelles += 1
    pourcentage = (nb_voyelles / taille_T) * 100 if taille_T > 0 else 0
    return pourcentage
def trouver_sous_chaine(T, sous_chaine):
    taille_T = taille(T)
    taille_sous_chaine = len(sous_chaine)
    for i in range(taille_T - taille_sous_chaine + 1):
        correspond = True
        for j in range(taille_sous_chaine):
            if T[i + j] != sous_chaine[j]:
                correspond = False
                break
        if correspond:
            return i
    return -1
def compter_occurrences(T, sous_chaine):
    nb_occurrences = 0
    taille_T = taille(T)
    taille_sous_chaine = len(sous_chaine)
    for i in range(taille_T - taille_sous_chaine + 1):
        correspond = True
        for j in range(taille_sous_chaine):
            if T[i + j] != sous_chaine[j]:
                correspond = False
                break
        if correspond:
            nb_occurrences += 1
    return nb_occurrences

T = list("bonjour wagon je suis wagon et je vais wagon\0")
sous_chaine = "wagon"
print("Taille de la chaîne :", taille(T))
print("Pourcentage de voyelles :", pourcentage_voyelles(T), "%")
index = trouver_sous_chaine(T, sous_chaine)
if index != -1:
    print(f"La sous-chaîne '{sous_chaine}' commence à l'indice {index}.")
else:
    print(f"La sous-chaîne '{sous_chaine}' n'est pas trouvée.")
print(f"Nombre d'occurrences de '{sous_chaine}' :", compter_occurrences(T, sous_chaine))
