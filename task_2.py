import random

list_number = random.choices(
    [k for k in range(random.choice(range(-1000, 1)), random.choice(range(1, 1000)))], k=20)

result = [list_number[i] for i in range(1, len(list_number)) if list_number[i] > list_number[i - 1]]
print(f"Для списка: {list_number} \nРезультатом будет список: {result}")
