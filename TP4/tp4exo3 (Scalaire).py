nMax = 3
v1 = []
v2 = []
x = 0.0

n = int(input("Input the size of vector : "))
while n > nMax or n < 1:
    n = int(input(f"\nSize may not be bigger than {nMax} or smaller than 1. Please try again.\nInput the size of vector : "))

print("\nSaisie du premier vecteur : ")
for i in range(n):
    y = int(input("Enter the value for v1 :"))
    v1.append(y)

print("\nSaisie du second vecteur : ")
for i in range(n):
    y = int(input("Enter the value for v2 :"))
    v2.append(y)

for i in range(n):
    x += v1[i] * v2[i]
print(f"\nLe produit scalaire de v1 par v2 vaut : {x}")
