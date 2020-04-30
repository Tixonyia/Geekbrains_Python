import random
with open("numbers_task_6.txt", "w") as numbers:
    for i in [round(random.uniform(-100, 100), 3) for i in range(0, 300)]:
        numbers.write(str(i) + ' ')
with open("numbers_task_6.txt", "r") as numbers:
    result = 0
    for i in numbers.readline().split():
        result += float(i)
print(round(result, 3))