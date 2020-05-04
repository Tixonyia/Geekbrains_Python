class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        Worker.__init__(self, name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f"Сотрудник {self.surname} {self.name} занимает должность: {self.position}.")

    def get_total_income(self):
        print(f"{self.surname} {self.name} заработал: {self._income['wage'] + self._income['bonus']}")


employee = Position(input("Name: "), input("Surname: "), input("Position: "), float(input("Wage: ")),
                    float(input("Bonus: ")))
print(employee.name, employee.surname, employee.position, employee._income['wage'], employee._income['bonus'])
employee.get_full_name()
employee.get_total_income()
