
notes = []
coefficients = []

for i in range(1, 6):
    input_values = input(f"Veuillez entrer la note du module {i} et le coefficient correspondant : ")
    note, coefficient = input_values.split()
    notes.append(float(note))
    coefficients.append(int(coefficient))

somme_ponderee = sum(note * coef for note, coef in zip(notes, coefficients))
somme_coefficients = sum(coefficients)

moyenne = somme_ponderee / somme_coefficients

admis = moyenne > 10 and all(note >= 8 for note in notes)


print(f"La moyenne générale est : {moyenne:.2f}")
if admis:
    print("L'étudiant est admis.")
else:
    print("L'étudiant n'est pas admis.")
