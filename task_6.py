import re

try:
    with open("for_task_6.txt", 'r') as file:
        result = {}
        for i in file.readlines():
            result[(i.split())[0].replace(":", '')] = (re.findall(r"(\d+)", i))
        for v in result.values():
            for i in range(0, len(v)):
                v[i] = float(v[i])
        for k, v in result.items():
            result[k] = sum(v)
        print(result)
except IOError:
    print("Output input error.")
