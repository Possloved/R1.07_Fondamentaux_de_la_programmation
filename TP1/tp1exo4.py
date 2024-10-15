dPassed = 0

minute = int(input("Entrer les minutes ecoulee depuis le debut du mois: "))

hPassed = minute/60
if hPassed > 23:
    dPassed = hPassed/24
dPassed = round(dPassed)

print("\nLe jour du mois est le:",dPassed)