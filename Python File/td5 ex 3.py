import random

day = random.randint(0,31)
hour = random.randint(0,24)
minute = random.randint(0,60)

dayH = day*24
totH = dayH+hour
hourToMinute = totH*60
totM = hourToMinute + minute


print("time since beginning month (minutes): ",totM )



