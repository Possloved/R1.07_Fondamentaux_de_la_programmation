def calcPrice(hStart, hEnd):
    if hStart < 0 or hStart > 23 or hEnd < 0 or hEnd > 23:
        return "Erreur. Heure doit être entre 0 & 24."
    if hStart == hEnd:
        return "Erreur. Heure de début et heure de fin identiques."
    if hStart > hEnd:
        return "Erreur. Heure de début plus tard que heure de fin."

    cout = 0
    tarif_1h = 0
    tarif_2h = 0

    for hour in range(hStart, hEnd):
        if 0 <= hour < 7 or 17 <= hour < 24:
            cout += 1
            tarif_1h += 1
        else:
            cout += 2
            tarif_2h += 1
    return cout, tarif_1h, tarif_2h


while True:
    try:
        hStart = int(input("Donnez l’heure de début de la location (un entier) : "))
        hEnd = int(input("Donnez l’heure de fin de la location (un entier) : "))
        result = calcPrice(hStart, hEnd)

        if isinstance(result, str):
            print(result)
        else:
            cout, tarif_1h, tarif_2h = result
            print(f"\nVous avez loué votre vélo pendant {tarif_1h} heure(s) au tarif horaire de 1.0 euro(s) "
                  f"et {tarif_2h} heure(s) au tarif horaire de 2.0 euro(s).")
            print(f"Le montant total à payer est de {cout} euro(s).")
        break
    except ValueError:
        print("Veuillez entrer les heures comme nombres entiers.")