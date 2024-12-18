import os
import sys

def recherche(dossier):
    listeFichiers, listeDossiers = [], []
    for root, dirs, files in os.walk(dossier):
        for file in files:
            listeFichiers.append(os.path.join(root, file))
        for dir in dirs:
            listeDossiers.append(os.path.join(root, dir))
    return listeFichiers, listeDossiers

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python find2.py <dossier>")
    else:
        dossier = sys.argv[1]
        if os.path.exists(dossier) and os.path.isdir(dossier):
            fichiers, dossiers = recherche(dossier)
            print("Fichiers :")
            print("\n".join(fichiers))
            print("Dossiers :")
            print("\n".join(dossiers))
        else:
            print("Erreur : le dossier spécifié n'existe pas.")
