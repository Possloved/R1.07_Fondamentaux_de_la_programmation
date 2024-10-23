while True:

    x = int(input("Enter a number: "))

    if (x>0) and (x%2==0):
        print("The number is positive & even.")
    elif (x<0) and (x%2==0):
        print("The number is negative & even.")
    elif (x>0) and (x%2==1):
        print("The number is positive & odd.")
    elif (x<0) and (x%2==1):
        print("The number is negative & odd.")
    else:
        print("The number is 0 (Zero).")