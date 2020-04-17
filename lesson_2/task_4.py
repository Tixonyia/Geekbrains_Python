user_string = input("Введите слова через пробел: ").split()
for i, k in enumerate(user_string):
    print(i, k if len(k) <= 10 else k[:10])
