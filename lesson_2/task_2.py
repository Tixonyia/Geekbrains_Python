user_list = list(input("Введите хоть что-то: "))
my_list = user_list.copy()
for i in range(len(my_list)):
    if i % 2 != 0:
        user_list[i], user_list[i - 1] = user_list[i - 1], user_list[i]
print(user_list)
