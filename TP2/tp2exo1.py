#Ecrire en Python un programme vous permettant de permuter les valeurs de deux variables contenant des entiers.

x = int(input("Enter Value X : "))
y = int(input("Enter value Y : "))

x, y = y, x

print("X =",x)
print("Y =",y)
