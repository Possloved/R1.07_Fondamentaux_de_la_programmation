x = float(input("Vous cherchez la table de multiplication de quel nombre ? : "))

for i in range(11):
    print(f"{x} * {i} = {round(x* i, 1)}")