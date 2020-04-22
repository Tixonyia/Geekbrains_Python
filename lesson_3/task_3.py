def my_func(number_1, number_2, number_3):
    """Принимает три аргумента.
    Позиционные аргументы:
    number_1:
    number_2:
    number_3:
    Проверяет корректность введённых данных.
    Возвращает сумму двух наибольших значений
    """
    while True:
        if number_1.replace(".", "", 1).replace("-", "", 1).isdigit() \
                and number_2.replace(".", "", 1).replace("-", "", 1).isdigit() \
                and number_3.replace(".", "", 1).replace("-", "", 1).isdigit():
            number_1, number_2, number_3 = float(number_1), float(number_2), float(number_3)
            numbers_sorted = sorted(list(locals().values()))
            result = numbers_sorted[len(numbers_sorted) - 1] + numbers_sorted[len(numbers_sorted) - 2]
            return result
        else:
            print("Нужно ввести три числа.")
            number_1 = input("Введите первое число: ")
            number_2 = input("Введите второе число: ")
            number_3 = input("Введите третье число: ")


print(my_func(input("Введите первое число: "), input("Введите второе число: "), input("Введите третье число: ")))
