
phrase = input("Entrez un mot ou une phrase : ")

phrase_epuree = "".join(c.lower() for c in phrase if c.isalpha())

if phrase_epuree == phrase_epuree[::-1]:
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")
