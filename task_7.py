import json
try:
    with open("for_task_7.txt", 'r') as file:
        data = []
        for i in file.readlines():
            i = i.split()
            data.append(i)
        data_dict = [{}, {}]
        index = 0
        average_profit = 0
        for i in data:
            if float(i[-2]) > float(i[-1]):
                average_profit += float(i[-2]) - float(i[-1])
                index += 1
                data_dict[0][i[0]] = float(i[-2]) - float(i[-1])
            elif float(i[-2]) < float(i[-1]):
                data_dict[0][i[0]] = float(i[-2]) - float(i[-1])
        data_dict[1]["average_profit"] = average_profit / index
        print(data_dict)
    with open("json_for_task_7.txt", 'w') as j:
        json.dump(data_dict, j, ensure_ascii=False, indent=1)

except IOError:
    print("Output input error.")
