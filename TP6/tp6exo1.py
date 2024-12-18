L1 = [0] * 3 #Initialisez une liste ne comprenant que trois zéros
print(L1, type(L1), id(L1))
#-------------------------------------
for elem in L1:
    print(elem, type(elem), id(elem))
#-------------------------------------
L1[1] += 1
print(L1, id(L1))
for elem in L1:
    print(elem, id(elem))
#--------------------------------------
chaine = "machaine"
print(id(chaine))
for char in chaine:
    print(char, id(char))