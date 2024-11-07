def isBissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)
def verifDate(date):
    if len(date) != 8 or not date.isdigit():
        return "Format incorrect. La date doit être au format jjmmaaaa avec uniquement des chiffres."

    jour = int(date[:2])
    mois = int(date[2:4])
    annee = int(date[4:])

    if mois < 1 or mois > 12:
        return "Date incorrecte : le mois doit être compris entre 1 et 12."

    jours_dans_mois = {
        1: 31, 2: 29 if isBissextile(annee) else 28, 3: 31,
        4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30,
        10: 31, 11: 30, 12: 31
    }

    if jour < 1 or jour > jours_dans_mois[mois]:
        return f"Date incorrecte : le jour doit être compris entre 01 et {jours_dans_mois[mois]} pour le mois {mois}."

    return "Date correcte."

dates = ["31021999", "31041000", "32052020", "30032021", "29022022"]
for date in dates:
    print(f"Vérification de la date {date} : {verifDate(date)}")
