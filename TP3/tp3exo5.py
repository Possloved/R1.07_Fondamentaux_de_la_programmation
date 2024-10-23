def calcPrice(hStart, hEnd):

    if hStart < 0 or hStart > 23 or hEnd< 0 or hEnd> 23:
        return "hour must be between 0 & 24 !"
    if hStart == hEnd:
        return "error. start and end time is identical"
    if hStart > hEnd:
        return "error. start time after end time"

    cout = 0
    for hour in range(hStart, hEnd):
        if 0 <= hour < 7 or 17 <= hour < 24:
            cout += 1
        else:
            cout += 2
    return cout

while True:
    try:
        hStart = int(input("hour start location : "))
        hEnd= int(input("hour end location : "))
        cout = calculer_cout(hStart, hEnd)
        if isinstance(cout, str):
            print(cout)
        else:
            print(f"price of the location is {cout} euros.")
        break
    except ValueError:
        print("enter hours as whole numbers")