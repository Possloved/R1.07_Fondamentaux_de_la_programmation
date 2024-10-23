def calculer_cout(heure_debut, heure_fin):
    """Calcule le coût de la location en fonction des heures de début et de fin.

    Args:
        heure_debut (int): Heure de début de la location.
        heure_fin (int): Heure de fin de la location.

    Returns:
        float: Coût total de la location.
    """

    # Vérification des heures
    if heure_debut < 0 or heure_debut > 23 or heure_fin < 0 or heure_fin > 23:
        return "Les heures doivent être comprises entre 0 et 24 !"
    if heure_debut == heure_fin:
        return "Attention ! l'heure de fin est identique à l'heure de début."
    if heure_debut > heure_fin:
        return "Attention ! le début de la location est après la fin ..."

    # Calcul du coût
    cout = 0
    for heure in range(heure_debut, heure_fin):
        if 0 <= heure < 7 or 17 <= heure < 24:
            cout += 1
        else:
            cout += 2
    return cout

# Programme principal
while True:
    try:
        heure_debut = int(input("Heure de début de la location : "))
        heure_fin = int(input("Heure de fin de la location : "))
        cout = calculer_cout(heure_debut, heure_fin)
        if isinstance(cout, str):
            print(cout)
        else:
            print(f"Le coût de la location est de {cout} euros.")
        break
    except ValueError:
        print("Veuillez entrer des heures sous forme d'entiers.")