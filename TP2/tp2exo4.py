base = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400

nbConvives = int(input("enter people eating : "))


nbConvives=int(input("Entrez le nombre de personne(s) conviées à la fondue : "))
fromage *=nbConvives / base
eau *=nbConvives / base
ail *=nbConvives / base
pain *=nbConvives / base
print(f"Pour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut :")
print(f"- {fromage:.1f} gr de fromage")
print(f"- {eau:.1f} dl d'eau")
print(f"- {ail:.1f} gousse(s) d'ail")
print(f"- {pain:.1f} gr de pain")