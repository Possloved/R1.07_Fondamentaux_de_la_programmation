day = int(input("Entrer le jour: "))
hour = int(input("Entrer l'heure: "))
minute = int(input("Entrer la minute: "))

dayH = day*24
totH = dayH+hour
hourToMinute = totH*60
totM = hourToMinute + minute


print("\nTemps ecoule depuis le debut du mois:",totM,"minutes.")