import itertools

while True:
    index = 0
    try:  # Ввод, проверка на числа
        initial_number, finite_number, step, repetitions = int(input("Enter initial number - ")), int(
            input("Enter finite number - ")), int(input("Enter step - ")), int(
            input("Enter the number of numbers in the list - "))
        # Перебор различных вариантов значений и шага. Сортровка относительно того куда "пойдет" список.
        if initial_number < finite_number and step > 0:
            index = 1
            break
        elif initial_number < finite_number and step < 0:
            initial_number, finite_number = finite_number, initial_number
            index = 2
            break
        elif initial_number > finite_number and step > 0:
            index = 3
            step = -step
            break
        elif initial_number > finite_number and step < 0:
            initial_number, finite_number, step = finite_number, initial_number, -step
            index = 4
            break
        elif initial_number == finite_number or step == 0:
            index = 5
            break

    except ValueError:
        print("Enter only whole numbers!")
list_numbers = []


def count_def(initial_def, finite_def, step_def):
    """
     Создаёт список чисел с заданным
     Принимает три позиционных аргумента
    """
    for i in itertools.count(initial_def, step_def):
        if index == 1 or index == 4:
            if i > finite_def:
                break
            else:
                list_numbers.append(i)
        elif index == 2 or index == 3:
            if i < finite_number:
                break
            else:
                list_numbers.append(i)
        elif index == 5:
            if step == 0:
                print("There are no numbers in the list in steps of 0.")
                break
            elif initial_number == finite_number:
                list_numbers.append(i)
                break


def cycle_def():
    """
    Создаёт список из элементов списка "list_numbers" согласно количеству repetitions".
    """
    result = []
    counter = 1
    for i in itertools.cycle(list_numbers):
        if counter > repetitions:
            print(result)
            break
        else:
            result.append(i)
            counter += 1


count_def(initial_number, finite_number, step)
cycle_def()
