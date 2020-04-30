try:
    with open("eng_sensible.txt", 'r') as eng_list:
        with open("rus_sensible.txt", "r") as rus_list:
            data = []
            eng_list = eng_list.readlines()
            rus_list = rus_list.readlines()
            for i in range(0, len(eng_list)):
                string = eng_list[i].split()
                data.append(" ".join(string).replace(string[0], str(rus_list[i].replace("\n", ''))))
    with open("result_task_4.txt", 'w') as result:
        for i in data:
            result.write(i + '\n')
except IOError:
    print("Output input error.")