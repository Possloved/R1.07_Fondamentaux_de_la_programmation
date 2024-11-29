nom = str(input("entrer votre nom: "))
prenom = str(input("entrer votre prenom: "))

nom = str.upper(nom)
prenom = str.lower(prenom)
prenom = str.capitalize(prenom)

print(f'{prenom} {nom}')