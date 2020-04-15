number = int(input("Введите целое положительное число: "))
max_numeral = 0
while number != 0:
    numeral = number % 10
    if numeral == 9:
        max_numeral = numeral
        break
    elif numeral > max_numeral:
        max_numeral = numeral
    number = number // 10

print(max_numeral)
