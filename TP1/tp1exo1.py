fName = str(input("Entrer le prénom: "))
lName = str(input("Entrer le nom: "))
math = float(input("Entrer la note de math: "))
english = float(input("Entrer la note d'anglais: "))
tech = float(input("Entrer la note de technologie: "))
year = int(input("Entrer l'année de graduation: "))

average = (math + english + tech)/3

print("\nfName est de type",type(fName))
print("lName est de type",type(lName))
print("math est de type",type(math))
print("english est de type",type(english))
print("tech est de type",type(tech))
print("year est de type",type(year))
print("\nL'étudiant {} {} de la promotion {} a une moyenne de {:.2f}.".format(fName, lName, year, average))