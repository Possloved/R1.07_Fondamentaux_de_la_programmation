import random

def generer(nbr, vmin, vmax):
    return [random.randint(vmin, vmax) for _ in range(nbr)]

def combienInferieur(table, vseuil):
    return sum(1 for x in table if x < vseuil)

nb = 100
print(f"Générer {nb} nombres entiers entre 0 et 100")
tab = generer(nb, 0, 100)
tab.sort()
print(tab)
total = combienInferieur(tab, 25)
print(f"Il y en a {total} inférieurs à 25")
#-------------------------------------
nb = int(input("Nombre de valeurs à générer : "))
vmin = int(input("Valeur minimale : "))
vmax = int(input("Valeur maximale : "))

seuil = 30
if input("Voulez-vous préciser le seuil ? (Oui/Non) ").lower() in ['oui', 'o']:
    seuil = int(input("Seuil : "))

tab = generer(nb, vmin, vmax)
tab.sort()
print(tab)
total = combienInferieur(tab, seuil)
print(f"Il y en a {total} inférieurs à {seuil}")
