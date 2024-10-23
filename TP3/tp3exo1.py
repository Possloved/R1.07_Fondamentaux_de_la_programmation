def somme_entiers(N):
    return N * (N + 1) // 2

N = int(input("Entrez un entier naturel N : "))
resultat = somme_entiers(N)
print("La somme des entiers de 0 à", N, "est :", resultat)

while True:
    valeur = int(input("Entrez une valeur (100 pour quitter) : "))
    if valeur == 100:
        break


valeurs = []
for _ in range(10):
    while True:
        valeur = float(input("Entrez une valeur entre 0 et 20 : "))
        if 0 <= valeur < 20:
            valeurs.append(valeur)
            break
        else:
            print("Valeur invalide. Veuillez réessayer.")

# Compter les valeurs dans chaque intervalle
moins_de_10 = sum(1 for v in valeurs if v < 10)
entre_10_et_15 = sum(1 for v in valeurs if 10 <= v < 15)
plus_de_15 = sum(1 for v in valeurs if v >= 15)

print("Nombre de valeurs inférieures à 10 :", moins_de_10)
print("Nombre de valeurs entre 10 et 15 :", entre_10_et_15)
print("Nombre de valeurs supérieures ou égales à 15 :", plus_de_15)

X = int(input("Entrez une valeur X supérieure à 1 : "))
N = 0
somme = 0
while somme <= X:
    N += 1
    somme = somme_entiers(N)
print("Le plus grand N est :", N - 1)