import random
list_number = random.choices(
    [k for k in range(random.choice(range(-10, 1)), random.choice(range(1, 10)))], k=10)
result = [list_number[i] for i in range(0, len(list_number)) if list_number.count(list_number[i]) == 1]
print(f"Для списка чисел: {list_number} \nСписок не повторяющихся элементов: {result}")