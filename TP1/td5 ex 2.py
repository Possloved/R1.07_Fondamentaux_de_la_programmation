day = int(input("enter day"))
hour = int(input("enter hour"))
minute = int(input("enter minute"))

dayH = day*24
totH = dayH+hour
hourToMinute = totH*60
totM = hourToMinute + minute


print("time since beginning month (minutes): ",totM )



