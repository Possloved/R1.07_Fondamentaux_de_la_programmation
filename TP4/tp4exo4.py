nmb=[]
v = int(input("Input size of list : "))

for i in range(v):
    y = int(input("Enter the value you want in the list :"))
    nmb.append(y)

mcn = 0
cm = 0
for val in nmb:

    x = nmb.count(val)
    if x > cm:
        mcn = val
        cm = x

print(f"\nLe nombre le plus frequent dans la liste est le : {mcn} ({cm} fois)")

