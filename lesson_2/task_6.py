number = 1
data = []
while True:
    date_user = input(
        "Введите характеристики товара через запятую: название, цена, количество, единица измерения. "
        "Или введите Отмена: ").split(
        ", ")
    if len(date_user) == 4:
        data_dict = {
            'название': date_user[0],
            'цена': date_user[1],
            'количество': date_user[2],
            'ед': date_user[3]
        }
        data.append((number, data_dict))
        number += 1
    elif date_user[0] == "Отмена":
        break
print(data)
analytics_dict = {}
name = []
price = []
quantity = []
units = []
for i in data:
    name.append(i[1]["название"])
    price.append(i[1]["цена"])
    quantity.append(i[1]["количество"])
    units.append(i[1]["ед"])
analytics_dict["название"] = name
analytics_dict["цена"] = price
analytics_dict["количество"] = quantity
analytics_dict["ед"] = units
print(analytics_dict)