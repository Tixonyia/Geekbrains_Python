result = 0


def amount(user_input_def):
    global result
    user_in_list = user_input_def.split()
    for i in user_in_list:
        if i.replace('.', '', 1).replace("-", "", 1).isdigit():
            i = float(i)
            result += i
        elif i == "Q":
            print(f"Вы вышли из программы. Сумма чисел равна - {round(result, 2)}")
            return "Q"
        else:
            print("Нужны только числа разделённые пробелом, либо Q для выхода.")


while True:
    user_input = input("Введте строку чисел, разделенных пробелом: ").upper()
    if amount(user_input) == "Q":
        break
    print(round(result, 2))

