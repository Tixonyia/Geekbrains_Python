my_list = [8, 8, 6, 5, 5, 3]
while True:
    number = input("Введите натуральное число: ")
    if number.isdigit():
        number = int(number)
        break
for i in range(len(my_list)):
    if number > my_list[i]:
        my_list.insert(i, number)
        break
    elif i == len(my_list) - 1:
        my_list.append(number)

print(f"Пользователь ввел число {number}. Результат: {' '.join(str(i) for i in my_list)}")
