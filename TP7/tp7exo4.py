import os
import sys

def recherche(dossier, fichier):
    listeFichiers = []
    for root, dirs, files in os.walk(dossier):
        for file in files:
            if file == fichier:
                listeFichiers.append(os.path.join(root, file))
    return listeFichiers

if __name__ == '__main__':
    if len(sys.argv) != 5 or sys.argv[1] != '-d' or sys.argv[3] != '-f':
        print("Usage: python find.py -d <dossier> -f <fichier>")
    else:
        dossier = sys.argv[2]
        fichier = sys.argv[4]
        if os.path.exists(dossier) and os.path.isdir(dossier):
            resultats = recherche(dossier, fichier)
            print("\n".join(resultats))
        else:
            print("Erreur : le dossier spécifié n'existe pas.")
