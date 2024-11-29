import os
import datetime
def afficher_informations(fichier):
    if os.path.isfile(fichier):
        taille = os.path.getsize(fichier)
        timestamp_modif = os.path.getmtime(fichier)
        date_modif = datetime.datetime.fromtimestamp(timestamp_modif)
        print(f"Fichier : {fichier}")
        print(f"Taille : {taille} octets")
        print(f"Date de dernière modification : {date_modif}")
        return timestamp_modif
    else:
        print(f"Le fichier {fichier} n'existe pas.")
        return None
fichier1 = input("Entrez le nom du premier fichier : ")
fichier2 = input("Entrez le nom du deuxième fichier : ")
modif_fichier1 = afficher_informations(fichier1)
modif_fichier2 = afficher_informations(fichier2)
if modif_fichier1 is not None and modif_fichier2 is not None:
    if modif_fichier1 > modif_fichier2:
        print(f"\nLe fichier le plus récent est : {fichier1}")
        print(f"Date de modification : {datetime.datetime.fromtimestamp(modif_fichier1)}")
    elif modif_fichier1 < modif_fichier2:
        print(f"\nLe fichier le plus récent est : {fichier2}")
        print(f"Date de modification : {datetime.datetime.fromtimestamp(modif_fichier2)}")
    else:
        print("\nLes deux fichiers ont été modifiés à la même date.")
