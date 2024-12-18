def ajouter_elt(lst=[0, 1, 2], elt=3):
    lst.append(elt)
    return lst

print(ajouter_elt())
#-------------------------------------
print(ajouter_elt())
print(id(ajouter_elt()))
#-------------------------------------
def ajouter_carac(ch="abc", elt="d"):
    return ch + elt

print(ajouter_carac())
