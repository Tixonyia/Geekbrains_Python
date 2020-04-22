string = input("Введите строку: ")
in_func = lambda x: string.title()
print(f"{in_func(string)}. Без сохранения регистра непервых заглавных букв.")
words = list(string)
words[0] = words[0].upper()
for i in range(len(words)):
    if words[i] == ' ':
        words[i + 1] = words[i + 1].upper()
result = "".join(words)
print(f"{result}. С сохранением регистра непервых заглавных букв.")