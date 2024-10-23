y = 1
z = 1
loop = 0
mult = 1
x = int(input("Enter value : "))

for i in range(x):
    y = y * mult
    mult += 1

while loop < x:
    loop = loop + 1
    z = z * loop

print("For loop : ", y)
print("While loop : ",z)