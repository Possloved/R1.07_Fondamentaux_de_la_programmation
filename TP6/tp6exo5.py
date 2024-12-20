import unicodedata
import string

def nettoyer_texte(texte):
    texte = ''.join(c for c in unicodedata.normalize('NFD', texte)
                    if unicodedata.category(c) != 'Mn')  # del accents
    texte = ''.join(c for c in texte if c.isalnum())  # del ponctuations
    return texte.lower()

def est_palindrome(texte):

    return texte == texte[::-1]

phrase = input("Entrez un mot ou une phrase : ")
if est_palindrome(phrase):
    print("C'est un palindrome.")
else:
    print("Ce n'est pas un palindrome.")
