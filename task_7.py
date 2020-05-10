class ComplexNumber:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    def __add__(self, other):
        i = '+'
        if self.number_2 + other.number_2 < 0:
            i = ""
        return f'{self.number_1 + other.number_1}{i}{self.number_2 + other.number_2}j'

    def __mul__(self, other):
        i = '+'
        if (self.number_2 * other.number_1) + (other.number_2 * self.number_1) < 0:
            i = ""
        return f'{(self.number_1 * other.number_1) - (self.number_2 * other.number_2)}{i}' \
               f'{(self.number_2 * other.number_1) + (other.number_2 * self.number_1)}j'


comp_1 = ComplexNumber(2, 3)
comp_2 = ComplexNumber(6, -94)
print(comp_1 + comp_2)
print(comp_1 * comp_2)
