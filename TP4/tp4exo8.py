infoEtudiant = {'firstname': 'Walter', 'name': 'White','promo': '2008','group': 'Breaking Bad'}
print(f"Votre prénom est '{infoEtudiant['firstname']}', votre nom est '{infoEtudiant['name']}', vous faites partie de la promo '{infoEtudiant['promo']}' et votre groupe est '{infoEtudiant['group']}'")

print("\nLes clés du dictionnaire sont :")
for key in infoEtudiant.keys():
    print(f"- {key}")
print("\nLes valeurs du dictionnaire sont :")
for value in infoEtudiant.values():
    print(f"- {value}")
print("\nLes tuplets du dictionnaire sont :")
for item in infoEtudiant.items():
    print(f"- {item}")

infoVoisin = {'firstname': 'Bruce','name': 'Wayne','promo': '2005','group': 'Batman Begins'}
print(f"\nL'autre étudiant a pour prénom '{infoVoisin['firstname']}', nom '{infoVoisin['name']}', promo '{infoVoisin['promo']}' et groupe '{infoVoisin['group']}'")

binome = {'id1': infoEtudiant,'id2': infoVoisin}
print("\nDictionnaire binôme :")
for idEtudiant, info in binome.items():
    print(f"ID : {idEtudiant}, Info : {info}")
print("\nLes étudiants formant le binôme sont :")
for idEtudiant, info in binome.items():
    print(f"- L'étudiant {info['firstname']} {info['name']} du groupe {info['group']}")