day_distance = float(input("С какой дистанции (в киллометрах) начнём?: "))
desired_distance = float(input("На какой (киллометрах) остановимся?: "))
day = 1
while day_distance <= desired_distance:
    day_distance = day_distance + day_distance * 0.1
    day += 1
print(f"Дистанция в {desired_distance} будет достигнута на {day} день.")
