import sys
import os

def aide():
    print("Usage: python find1.py <dossier>")

def affiche(dossier):
    for item in os.listdir(dossier):
        print(item)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        aide()
    else:
        dossier = sys.argv[1]
        if os.path.exists(dossier) and os.path.isdir(dossier):
            affiche(dossier)
        else:
            print("Erreur : le dossier spécifié n'existe pas.")
