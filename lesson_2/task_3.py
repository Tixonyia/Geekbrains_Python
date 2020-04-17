while True:
    month = input("Введите месяц в виде целочисленного чмсла от 1 до 12: ")
    if month.isdigit() and 1 <= int(month) <= 12:
        month = int(month)
        break
list_of_months = [
    "January", "February", "March",
    "April", "May", "June",
    "July", "August", "September",
    "October", "November", "December"
]

list_of_seasons = [
    "winter", "spring", "summer", "autumn"
]

if month in range(3) or month == 12:
    season = dict_key = list_of_seasons[0]
    dict_index = 0 if month == 12 else month
elif month in range(3, 6):
    season = dict_key = list_of_seasons[1]
    dict_index = month - 3
elif month in range(6, 9):
    season = dict_key = list_of_seasons[2]
    dict_index = month - 6
elif month in range(9, 12):
    season = dict_key = list_of_seasons[3]
    dict_index = month - 9
print(f"{list_of_months[month - 1]} is {season} month. From list.")

dict_of_season = {
    "winter": ["December", "January", "February"],
    "spring": ["March", "April", "May"],
    "summer": ["June", "July", "August"],
    "autumn": ["September", "October", "November"]
}
print(f"{dict_of_season[dict_key][dict_index]} is {dict_key} month. From dict.")
