import random

rNumber = random.randint(0,99)
guess = int(input("Try to guess the number : "))
count = 1

while guess != rNumber:
    if rNumber > guess:
        print("The number is bigger !")
    elif rNumber < guess:
        print("The number is smaller !")
    count += 1
    guess = int(input("\nTry to guess the number :"))

print("\nYou guessed the number corretly!")
print("The number was",rNumber,".")
print("You guessed in ",count,"tries.")