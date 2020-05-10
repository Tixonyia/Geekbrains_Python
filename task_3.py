class OwnError(Exception):
    def __init__(self, text):
        self.text = text


print("For exit enter 'Q'.")
result = []
while True:
    try:
        user_enter = input("Enter numbers:\n")
        if user_enter.upper() == "Q":
            break
        user_enter = user_enter.split()
        [result.append(i) for i in user_enter if i.replace("-", '').isdigit()]
        for i in user_enter:
            if not i.replace("-", '').isdigit():
                raise OwnError("There are lines.")
    except OwnError as own_error:
        print(own_error)
print(result)