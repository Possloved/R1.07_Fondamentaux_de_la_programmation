import time

x = int(input("Enter value : "))
y = x

print("\nFor loop:")
for i in range (x):
    print(x)
    x -= 1
    time.sleep(0.5)

print("\nWhile loop:")
while y > 0:
    print(y)
    y -= 1
    time.sleep(0.5)