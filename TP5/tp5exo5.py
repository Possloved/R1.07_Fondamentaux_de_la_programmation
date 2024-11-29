heures_travaillees = float(input("Entrez le nombre d'heures travaillées : "))
salaire_horaire = float(input("Entrez le salaire horaire : "))

if heures_travaillees <= 160:
    salaire = heures_travaillees * salaire_horaire
elif heures_travaillees <= 200:
    salaire = 160 * salaire_horaire + (heures_travaillees - 160) * salaire_horaire * 1.25
else:
    salaire = 160 * salaire_horaire + 40 * salaire_horaire * 1.25 + (heures_travaillees - 200) * salaire_horaire * 1.5

print(f"Le salaire total de l'ouvrier est : {salaire:.2f} euros.")
