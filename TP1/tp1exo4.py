minute = int(input("enter minute passed:"))
dPassed = 0

hPassed = minute/60
if hPassed > 23:
    dPassed = hPassed/24
dPassed = round(dPassed)


print("current day of the month is the",dPassed)
