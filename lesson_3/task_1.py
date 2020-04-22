def division(number_1_def, number_2_def):
    """Выполняет деление
    number_1_def -- делимое
    number_2_def -- делитель
    replace(".", "", 1).replace("-", "", 1).isdigit() -- способ проверки на содержание действительных чисел
    """
    while True:
        if number_1_def.replace(".", "", 1).replace("-", "", 1).isdigit() \
                and number_2_def.replace(".", "", 1).replace("-", "", 1).isdigit():
            number_1_def, number_2_def = float(number_1_def), float(number_2_def)
            try:
                print(round((number_1_def / number_2_def), 2))
                break
            except ZeroDivisionError:
                print("А Марья Ивановна говорит, что на ноль делить нельзя!")
                number_1_def = input("Введите первое число: ")
                number_2_def = input("Введите второе число: ")
        else:
            print("Нужно ввести два числа.")
            number_1_def = input("Введите первое число: ")
            number_2_def = input("Введите второе число: ")


division(input("Введите первое число: "), input("Введите второе число: "))
