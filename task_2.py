class OwnError(Exception):
    def __init__(self, text):
        self.text = text


print("For exit enter 'Q'")
while True:
    try:
        number_1 = input("Enter dividend: ")
        if number_1.upper() == "Q":
            break
        number_2 = input("Enter divider: ")
        if number_2.upper() == "Q":
            break
        if float(number_2) == 0:
            raise OwnError("Divisor cannot be zero.")
        else:
            print(f"Division result: {round(float(number_1) / float(number_2), 3)}.")
    except OwnError as own_error:
        print(own_error)
    except ValueError:
        print("Enter only two numbers.")
