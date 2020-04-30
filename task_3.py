try:
    with open("List_for_task_3.txt", "r") as file:
        total_all = [0, 0]
        total_less_than_20 = [0, 0]
        for i in file.readlines():
            i = i.split()
            total_all[0] += 1
            total_all[1] += float(i[-1])
            if float(i[-1]) < 20000:
                total_less_than_20[0] += 1
                total_less_than_20[1] += float(i[-1])
                print(i[1])
        print(f"Average salary of all employees: {round(total_all[1] / total_all[0], 2)}")
        print(f"Average salary of employees with a salary of less than 20,000:"
              f" {round(total_less_than_20[1] / total_less_than_20[0], 2)}")
except IOError:
    print("Output input error.")