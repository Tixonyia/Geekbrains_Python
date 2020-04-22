def data_user_def(name_def, surname_def, year_def, city_def, email_def, telephone_number_def):
    for i in list(locals().values()):
        print(i, end=" ")


while True:
    data_user = input("Введите  имя, фамилия, год рождения, город проживания, email и телефон: ").split(", ")
    if len(data_user) == 6:
        data_user_def(telephone_number_def=data_user[5], name_def=data_user[0], surname_def=data_user[1],
                      year_def=data_user[2],
                      city_def=data_user[3],
                      email_def=data_user[4])
        break
    else:
        print("Введите данные через запятую в количестве 6.")

