import random
def lancer():
    x = random.randint(0,99)

    if x <= 66:
        return True
    else:
        return False
    return x

print(lancer())