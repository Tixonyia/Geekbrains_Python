class Cell:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        try:
            if int(self.number > 0):
                return str(f"Number of cells in a cell: {self.number}.")
            else:
                return "There is at least one cell in a living cell"
        except ValueError:
            return "Enter correct data."

    def __add__(self, other):
        try:
            if int(self.number) > 0 and int(other.number) > 0:
                return int(self.number) + int(other.number)
            else:
                return "Enter correct data."
        except ValueError:
            return "Enter correct data."

    def __sub__(self, other):
        try:
            if int(self.number) > 0 and int(other.number) > 0:
                if int(self.number) - int(other.number) >= 0:
                    return self.number - other.number
                else:
                    return "Subtraction cannot be made from the smaller."
            else:
                return "Enter correct data."
        except ValueError:
            return "Enter correct data."

    def __mul__(self, other):
        try:
            if int(self.number) > 0 and int(other.number) > 0:
                return int(self.number * other.number)
            else:
                return "Enter correct data."
        except ValueError:
            return "Enter correct data."

    def __truediv__(self, other):
        try:
            if int(self.number) > 0 and int(other.number) > 0:
                return self.number // other.number
            else:
                return "Enter correct data."
        except ValueError:
            return "Enter correct data."

    def make_order(self, number_of_columns):
        numbers_stars = self.number // number_of_columns
        balance = self.number - numbers_stars * number_of_columns
        result = f"{'*' * number_of_columns}\n" * numbers_stars + f'{"*" * balance}'
        return result


cell_1 = Cell(923)
cell_2 = Cell(23)
print(cell_1)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_2.make_order(3))
