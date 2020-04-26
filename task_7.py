import math

while True:
    try:
        number = int(input("Enter factorial of a number - "))
        if number <= 0:
            print("Enter only whole positive numbers!")
        else:
            break
    except ValueError:
        print("Enter only whole positive numbers!")


def fact():
    for el in range(1, number + 1):
        el = math.factorial(el)
        yield el


for i in fact():
    print(i)
