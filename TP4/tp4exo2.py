import statistics
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
notes = []



for i in range(nombreEtudiants):
    x = float(input(f"Note etudiant {i+1} : "))
    while x > 20 or x < 0:
        x = float(input(f"La valeur de la note ne peut pas etre plus bas que 0 ou plus grande que 20.\nNote etudiant {i + 1} : "))

    notes.append(x)

print("\nMoyenne de classe : ",statistics.mean(notes))

print("\nNuméro de l’Etudiant | note | ecart a la moyenne")
for i in range(nombreEtudiants):
    print(f"{i} | {notes[i]} | {notes[i] - statistics.mean(notes)}")