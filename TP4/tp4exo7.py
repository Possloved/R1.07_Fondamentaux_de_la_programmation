binome = ('login1', 'login2')

print(f"L'étudiant {binome[0]} est en binôme avec l'étudiant {binome[1]}")

# DEL only one '#' in one of the two following lines, it's to display what type of error will happen.
# binome[1] = 'nouveau_login'
# del binome[1]

binome = binome + ('login3',)
print(f"Le trinôme est composé de {binome}")
