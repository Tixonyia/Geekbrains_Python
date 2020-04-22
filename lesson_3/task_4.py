def negative_degree(x, y):
    while True:
        if x.replace(".", "", 1).isdigit() and y.replace("-", "", 1).isdigit() and int(y) < 0:
            x, y = float(x), int(y)
            divider = 1
            result_1 = round((x ** y), 6)
            for i in range(abs(y)):
                divider *= x
            result_2 = round((1 / divider), 6)
            print(f"{result_1} - возведение в степень с помощью оператора **")
            print(f"{result_2} - возведение в степень без оператора **")
            break
        else:
            x = input("Нужно ввести действительное положительное основание степени: ")
            y = input("Нужно ввести целый отрицательный показатель степени: ")


negative_degree(input("Введите действительное положительное основание степени: "),
                input("Введите целый отрицательный показатель степени: "))
